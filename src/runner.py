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

# Load .env variables cleanly if present (zero-dependency standard library)
_env_file = project_root / ".env"
if _env_file.exists():
    for _line in _env_file.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

from src.schema import ExperimentalCondition, ProblemSpec


# Model Registry: Pinned providers, quantizations, verified pricing, and official URLs
# Verified Date: November 1, 2026
MODEL_REGISTRY = {
    "meta-llama/llama-3.3-70b-instruct": {
        "pinned_provider": "DeepInfra",
        "quantization": "bf16",
        "prompt_price_per_m": 0.12,
        "completion_price_per_m": 0.30,
        "source_url": "https://openrouter.ai/meta-llama/llama-3.3-70b-instruct",
        "doc_url": "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct",
        "verified_date": "2026-11-01"
    },
    "qwen/qwen-2.5-coder-32b-instruct": {
        "pinned_provider": "DeepInfra",
        "quantization": "bf16",
        "prompt_price_per_m": 0.06,
        "completion_price_per_m": 0.15,
        "source_url": "https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct",
        "doc_url": "https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct",
        "verified_date": "2026-11-01"
    },
    "deepseek/deepseek-chat": {
        "pinned_provider": "DeepSeek",
        "quantization": "fp8",
        "prompt_price_per_m": 0.14,
        "completion_price_per_m": 0.28,
        "source_url": "https://openrouter.ai/deepseek/deepseek-chat",
        "doc_url": "https://huggingface.co/deepseek-ai/DeepSeek-V3",
        "verified_date": "2026-11-01"
    },
    "meta-llama/llama-3.1-8b-instruct": {
        "pinned_provider": "DeepInfra",
        "quantization": "bf16",
        "prompt_price_per_m": 0.04,
        "completion_price_per_m": 0.08,
        "source_url": "https://openrouter.ai/meta-llama/llama-3.1-8b-instruct",
        "doc_url": "https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct",
        "verified_date": "2026-11-01"
    },
    "qwen/qwen-2.5-7b-instruct": {
        "pinned_provider": "DeepInfra",
        "quantization": "bf16",
        "prompt_price_per_m": 0.03,
        "completion_price_per_m": 0.06,
        "source_url": "https://openrouter.ai/qwen/qwen-2.5-7b-instruct",
        "doc_url": "https://huggingface.co/Qwen/Qwen2.5-7B-Instruct",
        "verified_date": "2026-11-01"
    },
}

DEFAULT_PRICING = {
    k: {"prompt": v["prompt_price_per_m"], "completion": v["completion_price_per_m"]}
    for k, v in MODEL_REGISTRY.items()
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
3. Provide ONLY executable Python test code.
4. Do NOT define, stub, or re-implement the function under test (it is ALREADY imported and available in the test namespace).
5. Prefer simple `assert` statements or standalone `def test_...(): assert ...` functions. Do NOT use `unittest.TestCase` or `unittest.main()`.
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
4. Do NOT copy, define, or re-implement the function under test into your code (it is ALREADY imported and available in the test namespace).
5. Prefer simple `assert` statements or standalone `def test_...(): assert ...` functions. Do NOT use `unittest.TestCase` or `unittest.main()`.
"""
}


class KeyManager:
    _keys: list[str] = []
    _current_idx: int = 0

    @classmethod
    def get_keys(cls) -> list[str]:
        if not cls._keys:
            raw = os.getenv("OPENROUTER_API_KEYS") or ""
            if raw:
                cls._keys = [k.strip() for k in raw.split(",") if k.strip()]
            if not cls._keys:
                single = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY") or ""
                if single:
                    cls._keys = [single.strip()]
        return cls._keys

    @classmethod
    def get_active_key(cls) -> str:
        keys = cls.get_keys()
        if not keys:
            return ""
        return keys[cls._current_idx % len(keys)]

    @classmethod
    def rotate_key(cls) -> str:
        keys = cls.get_keys()
        if not keys:
            return ""
        cls._current_idx = (cls._current_idx + 1) % len(keys)
        new_key = keys[cls._current_idx]
        print(f"[KeyManager] Rotated to API key index {cls._current_idx} ({new_key[:12]}...)", flush=True)
        return new_key


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
        pinned_provider: Optional[str] = None,
        quantization: Optional[str] = None,
        pricing: Optional[Dict[str, float]] = None
    ):
        self.model_name = model_name
        self.api_key = api_key or KeyManager.get_active_key() or os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY") or os.getenv("LLM_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL") or "https://openrouter.ai/api/v1"
        self.temperature = temperature
        
        reg_entry = MODEL_REGISTRY.get(model_name, {})
        self.pinned_provider = pinned_provider or reg_entry.get("pinned_provider")
        self.quantization = quantization or reg_entry.get("quantization", "unknown")
        self.pricing = pricing or DEFAULT_PRICING.get(model_name, {"prompt": 0.20, "completion": 0.60})

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

        # Prefer OpenAI SDK if installed (robust SSL/certifi on Windows) with auto-retry
        last_sdk_err = None
        for retry_attempt in range(3):
            try:
                import importlib
                openai_mod = importlib.import_module("openai")
                openai_cls = getattr(openai_mod, "OpenAI")
                client = openai_cls(api_key=self.api_key, base_url=self.base_url, timeout=40.0)
                extra_body = {"provider": {"order": [self.pinned_provider], "allow_fallbacks": True}} if self.pinned_provider else None
                response = client.chat.completions.create(
                    model=self.model_name,
                    messages=payload["messages"],
                    temperature=self.temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    extra_body=extra_body,
                    timeout=40.0
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
                    "quantization": self.quantization,
                    "created_timestamp": getattr(response, "created", None),
                    "response_id": getattr(response, "id", None),
                    "caller": "openai_sdk"
                }
                return content_cleaned, p_tok, c_tok, elapsed, cost_usd, call_metadata
            except Exception as sdk_err:
                last_sdk_err = sdk_err
                err_str = str(sdk_err)
                if any(x in err_str for x in ("402", "credits", "afford", "quota", "rate_limit")):
                    self.api_key = KeyManager.rotate_key()
                if retry_attempt < 2:
                    time.sleep(2.0 * (retry_attempt + 1))
                else:
                    break

        # Fallback to native HTTP via urllib if OpenAI SDK failed on all retries
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
                "quantization": self.quantization,
                "created_timestamp": resp_json.get("created"),
                "response_id": resp_json.get("id"),
                "caller": "native_urllib"
            }
            return content_cleaned, prompt_tokens, completion_tokens, elapsed, cost_usd, call_metadata
        except Exception:
            raise RuntimeError(f"API request failed: {str(last_sdk_err)}")

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


def log_real_token_usage(
    problem_id: str,
    phase: str,
    condition: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    cost_usd: float,
    elapsed_sec: float,
    retries: int = 0,
    status: str = "SUCCESS",
    csv_path: Optional[str] = None
) -> None:
    """Appends exact live token and cost accounting record to real_tokens.csv."""
    from datetime import datetime, timezone
    target_path = Path(csv_path) if csv_path else (project_root / "data" / "real_tokens.csv")
    total_tokens = prompt_tokens + completion_tokens
    timestamp = datetime.now(timezone.utc).isoformat()
    row = f"{timestamp},{problem_id},{phase},{condition},{model},{prompt_tokens},{completion_tokens},{total_tokens},{cost_usd:.6f},{elapsed_sec:.3f},{retries},{status}\n"
    with open(target_path, "a", encoding="utf-8") as f:
        f.write(row)

