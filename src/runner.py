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


# Pricing catalog ($ per 1 Million tokens) - updated for empirical cost calculation
DEFAULT_PRICING = {
    "gpt-4o-2024-08-06": {"prompt": 2.50, "completion": 10.00},
    "gpt-4o-mini": {"prompt": 0.15, "completion": 0.60},
    "claude-3-5-sonnet-20241022": {"prompt": 3.00, "completion": 15.00},
    "deepseek-chat": {"prompt": 0.14, "completion": 0.28},
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
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("Please install openai package via `pip install openai` to execute API calls.")

        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        start = time.perf_counter()

        extra_body = {}
        if self.pinned_provider:
            # Enforce exact provider in OpenRouter to eliminate non-deterministic routing
            extra_body["provider"] = {
                "order": [self.pinned_provider],
                "allow_fallbacks": False
            }

        response = client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=max_tokens,
            stop=stop,
            extra_body=extra_body if extra_body else None
        )
        elapsed = time.perf_counter() - start

        content = response.choices[0].message.content or ""
        content_cleaned = self._clean_code_fences(content)

        usage = response.usage
        prompt_tokens = usage.prompt_tokens if usage else len(prompt.split()) * 2
        completion_tokens = usage.completion_tokens if usage else len(content.split()) * 2

        cost_usd = (
            (prompt_tokens / 1_000_000.0) * self.pricing.get("prompt", 0.0) +
            (completion_tokens / 1_000_000.0) * self.pricing.get("completion", 0.0)
        )

        call_metadata = {
            "model_requested": self.model_name,
            "system_fingerprint": getattr(response, "system_fingerprint", None),
            "pinned_provider": self.pinned_provider,
            "created_timestamp": getattr(response, "created", None),
            "response_id": getattr(response, "id", None)
        }

        return content_cleaned, prompt_tokens, completion_tokens, elapsed, cost_usd, call_metadata

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
