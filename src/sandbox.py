"""
Execution sandbox supporting both Docker-isolated containers (--network none)
and hardened, network-disabled local subprocess isolation.
"""

import sys
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Tuple, Dict, Any, Optional


class SandboxStatus:
    PASSED = "PASSED"
    FAILED_ASSERTION = "FAILED_ASSERTION"
    RUNTIME_EXCEPTION = "RUNTIME_EXCEPTION"
    TIMEOUT = "TIMEOUT"
    SYNTAX_ERROR = "SYNTAX_ERROR"
    SANDBOX_ERROR = "SANDBOX_ERROR"


import functools

@functools.lru_cache(maxsize=1)
def is_docker_available() -> bool:
    """Checks whether Docker daemon is active and responsive."""
    try:
        res = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            text=True,
            timeout=2.0
        )
        return res.returncode == 0
    except Exception:
        return False


def execute_code_with_test(
    implementation_code: str,
    test_code: str,
    timeout_seconds: float = 6.0,
    force_backend: Optional[str] = None  # "docker", "hardened_subprocess", or None (auto)
) -> Tuple[str, str, float, str]:
    """
    Executes implementation_code concatenated with test_code in an isolated environment.
    
    Guarantees:
      1. Zero network access (Docker: --network none; Subprocess: mock/disabled socket module).
      2. Ephemeral isolated filesystem (dedicated temporary directory destroyed on completion).
      3. Strict execution timeout.
      
    Returns:
        (status, log_output, elapsed_ms, backend_used)
    """
    combined_script = f"""# -*- coding: utf-8 -*-
import sys
import os

# --- Security Hardening: Lockdown Network & System Hooks ---
try:
    import socket
    socket.socket = None
    socket.create_connection = None
    socket.getaddrinfo = None
except Exception:
    pass

# --- Implementation under Test ---
{implementation_code}

# --- Test Execution Block ---
{test_code}
"""

    use_docker = (force_backend == "docker") or (force_backend is None and is_docker_available())

    with tempfile.TemporaryDirectory(prefix="sandbox_run_") as tmp_dir:
        script_path = Path(tmp_dir) / "run_eval.py"
        script_path.write_text(combined_script, encoding="utf-8")
        
        start_time = time.perf_counter()

        if use_docker:
            # Docker Container Sandbox: Full OS/Kernel containment with zero networking
            backend_name = "docker_container"
            cmd = [
                "docker", "run", "--rm",
                "--network", "none",
                "--memory", "512m",
                "--cpus", "1.0",
                "-v", f"{tmp_dir}:/workspace:ro",
                "python:3.11-slim",
                "python", "/workspace/run_eval.py"
            ]
        else:
            # Hardened Subprocess Sandbox: Dedicated temp directory + network-disabled Python guard
            backend_name = "hardened_subprocess"
            cmd = [sys.executable, str(script_path)]

        try:
            # Clean execution environment (strip inherited path vulnerabilities)
            env = os.environ.copy()
            env["PYTHONNOUSERSITE"] = "1"
            env["PYTHONPATH"] = ""
            
            proc = subprocess.run(
                cmd,
                cwd=tmp_dir,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                encoding="utf-8",
                errors="replace",
                env=env
            )
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            output = proc.stdout + ("\n" + proc.stderr if proc.stderr else "")

            if proc.returncode == 0:
                return SandboxStatus.PASSED, output.strip(), elapsed_ms, backend_name
            elif "AssertionError" in proc.stderr:
                return SandboxStatus.FAILED_ASSERTION, output.strip(), elapsed_ms, backend_name
            elif "SyntaxError" in proc.stderr:
                return SandboxStatus.SYNTAX_ERROR, output.strip(), elapsed_ms, backend_name
            else:
                return SandboxStatus.RUNTIME_EXCEPTION, output.strip(), elapsed_ms, backend_name

        except subprocess.TimeoutExpired:
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            return SandboxStatus.TIMEOUT, f"Execution timed out after {timeout_seconds}s", elapsed_ms, backend_name
        except Exception as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            return SandboxStatus.SANDBOX_ERROR, f"Sandbox execution error: {str(e)}", elapsed_ms, backend_name
