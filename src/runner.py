"""
API Runner and LLM Orchestrator for the 2x2 Factorial Code-First Testing Experiment.
Manages prompts, model invocations, exact version tracking, token accounting, and cost logging.
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.schema import ExperimentalCondition, ProblemSpec


# Pricing catalog ($ per 1 Million tokens) - OpenRouter rates verified November 2026
DEFAULT_PRICING = {
    "meta-llama/llama-3.3-70b-instruct": {"prompt": 0.12, "completion": 0.30},
    "qwen/qwen-2.5-coder-32b-instruct": {"prompt": 0.06, "completion": 0.15},
    "deepseek/deepseek-chat": {"prompt": 0.15, "completion": 0.60},
    "openai/gpt-4o-mini": {"prompt": 0.15, "completion": 0.60},
}


PROMPT_TEMPLATES = {
    "coder": """You are an expert Python software engineer. Write a complete, correct, and self-contained Python implementation for the function described below.

Function Signature:
{signature}

Specification:
{docstring}

Instructions:
1. Provide ONLY valid, executable Python code for the function.
2. Do NOT wrap the code in conversational explanation.
3. Use standard type hints and adhere strictly to the specification.
""",

    "test_spec_only": """You are an expert Python QA engineer. Write a suite of comprehensive unit tests to thoroughly verify the behavior of the following function based ONLY on its specification.

Function Signature:
{signature}

Specification:
{docstring}

Instructions:
1. Write 3 to 6 distinct unit test assertions or test functions (e.g., `def test_...(): assert ...`).
2. Test standard inputs, edge cases (empty inputs, bounds), and exception behavior if specified.
3. Provide ONLY executable Python test code. Do NOT provide the implementation.
4. Each test must be completely self-contained.
""",

    "test_code_first": """You are an expert Python QA engineer. Write a suite of comprehensive unit tests to thoroughly verify the behavior of the following function. You are provided with its specification and an implementation.

Function Signature:
{signature}

Specification:
{docstring}

Implementation under Test:
```python
{implementation}
```

Instructions:
1. Write 3 to 6 distinct unit test assertions or test functions (e.g., `def test_...(): assert ...`).
2. Test standard inputs, edge cases (empty inputs, bounds), and exception behavior if specified.
3. Provide ONLY executable Python test code.
4. Each test must be completely self-contained.
"""
}


class LLMClient:
    """
    Unified client supporting OpenAI-compatible endpoints (OpenAI, DeepSeek, OpenRouter).
    Includes OpenRouter provider pinning to enforce exact hardware/quantization reproducibility.
    """
    def __init__(
        self,
        model_name: str,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        temperature: float = 0.2,
        pinned_provider: Optional[str] = None,  # e.g., "Anthropic", "OpenAI", "DeepSeek"
        pricing: Optional[Dict[str, float]] = None
    ):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY") or os.getenv("LLM_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL") or "https://openrouter.ai/api/v1"
        self.temperature = temperature
        self.pinned_provider = pinned_provider
        self.pricing = pricing or DEFAULT_PRICING.get(model_name, {"prompt": 2.0, "completion": 8.0})

    def generate(
        self,
        prompt: str,
        max_tokens: int = 1500,
        stop: Optional[list] = None
    ) -> Tuple[str, int, int, float, float, Dict[str, Any]]:
        """
        Executes generation and returns:
            (generated_text, prompt_tokens, completion_tokens, elapsed_seconds, cost_usd, call_metadata)
        """
        start = time.perf_counter()

        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature,
            "max_tokens": max_tokens
        }
        if stop:
            payload["stop"] = stop
        if self.pinned_provider:
            payload["provider"] = {
                "order": [self.pinned_provider],
                "allow_fallbacks": False
            }

        # Try native HTTP via urllib first (zero external dependencies required)
        try:
            import urllib.request
            import urllib.error

            endpoint = self.base_url.rstrip("/") + "/chat/completions"
            req_data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                endpoint,
                data=req_data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key or ''}",
                    "User-Agent": "CodeFirstTestingBenchmark/1.0"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=30.0) as resp:
                resp_json = json.loads(resp.read().decode("utf-8"))
            
            elapsed = time.perf_counter() - start
            choices = resp_json.get("choices", [])
            content = choices[0]["message"]["content"] if choices else ""
            content_cleaned = self._clean_code_fences(content)

            usage = resp_json.get("usage", {})
            prompt_tokens = usage.get("prompt_tokens", len(prompt.split()) * 2)
            completion_tokens = usage.get("completion_tokens", len(content.split()) * 2)

            cost_usd = (
                (prompt_tokens / 1_000_000.0) * self.pricing.get("prompt", 0.0) +
                (completion_tokens / 1_000_000.0) * self.pricing.get("completion", 0.0)
            )

            call_metadata = {
                "model_requested": self.model_name,
                "system_fingerprint": resp_json.get("system_fingerprint"),
                "pinned_provider": self.pinned_provider,
                "created_timestamp": resp_json.get("created"),
                "response_id": resp_json.get("id"),
                "caller": "native_urllib"
            }
            return content_cleaned, prompt_tokens, completion_tokens, elapsed, cost_usd, call_metadata
        except Exception as urllib_err:
            # Fallback to openai SDK if installed (dynamically loaded to avoid static linter errors)
            try:
                import importlib
                openai_mod = importlib.import_module("openai")
                openai_cls = getattr(openai_mod, "OpenAI")
                client = openai_cls(api_key=self.api_key, base_url=self.base_url)
                extra_body = {"provider": payload["provider"]} if "provider" in payload else None
                response = client.chat.completions.create(
                    model=self.model_name,
                    messages=payload["messages"],
                    temperature=self.temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    extra_body=extra_body
                )
                elapsed = time.perf_counter() - start
                content = response.choices[0].message.content or ""
                content_cleaned = self._clean_code_fences(content)
                usage = response.usage
                p_tok = usage.prompt_tokens if usage else len(prompt.split()) * 2
                c_tok = usage.completion_tokens if usage else len(content.split()) * 2
                cost_usd = (
                    (p_tok / 1_000_000.0) * self.pricing.get("prompt", 0.0) +
                    (c_tok / 1_000_000.0) * self.pricing.get("completion", 0.0)
                )
                call_metadata = {
                    "model_requested": self.model_name,
                    "system_fingerprint": getattr(response, "system_fingerprint", None),
                    "pinned_provider": self.pinned_provider,
                    "created_timestamp": getattr(response, "created", None),
                    "response_id": getattr(response, "id", None),
                    "caller": "openai_sdk"
                }
                return content_cleaned, p_tok, c_tok, elapsed, cost_usd, call_metadata
            except Exception:
                raise RuntimeError(f"API request failed: {str(urllib_err)}")

    @staticmethod
    def _clean_code_fences(text: str) -> str:
        """Strips ```python ... ``` markdown formatting if the model wrapped output."""
        lines = text.strip().splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        return "\n".join(lines).strip()


def run_coder_phase(problem: ProblemSpec, coder_client: LLMClient) -> Dict[str, Any]:
    """Generates candidate implementation from specification."""
    prompt = PROMPT_TEMPLATES["coder"].format(
        signature=problem.signature,
        docstring=problem.docstring
    )
    code, p_tok, c_tok, elapsed, cost, meta = coder_client.generate(prompt)
    return {
        "problem_id": problem.problem_id,
        "coder_model": coder_client.model_name,
        "candidate_code": code,
        "prompt_tokens": p_tok,
        "completion_tokens": c_tok,
        "elapsed_sec": round(elapsed, 3),
        "cost_usd": round(cost, 6),
        "meta": meta
    }


def run_oracle_phase(
    problem: ProblemSpec,
    condition: ExperimentalCondition,
    tester_client: LLMClient,
    faulty_code: Optional[str] = None
) -> Dict[str, Any]:
    """Generates test suite under the designated 2x2 experimental condition."""
    if condition in (ExperimentalCondition.T0_SPEC_SAME, ExperimentalCondition.T3_SPEC_CROSS):
        prompt = PROMPT_TEMPLATES["test_spec_only"].format(
            signature=problem.signature,
            docstring=problem.docstring
        )
    else:
        if not faulty_code:
            raise ValueError(f"Condition {condition} requires faulty_code to be provided.")
        prompt = PROMPT_TEMPLATES["test_code_first"].format(
            signature=problem.signature,
            docstring=problem.docstring,
            implementation=faulty_code
        )

    test_code, p_tok, c_tok, elapsed, cost, meta = tester_client.generate(prompt)
    return {
        "problem_id": problem.problem_id,
        "condition": condition.value,
        "tester_model": tester_client.model_name,
        "generated_test": test_code,
        "prompt_tokens": p_tok,
        "completion_tokens": c_tok,
        "elapsed_sec": round(elapsed, 3),
        "cost_usd": round(cost, 6),
        "meta": meta
    }
