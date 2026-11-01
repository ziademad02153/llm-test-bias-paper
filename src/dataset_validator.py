"""
Validator script to inspect candidate problems before inclusion in the dataset.
Ensures C_ref strictly passes 100% on T_ref and metadata is fully specified.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, Tuple

# Ensure project root is in sys.path when invoked directly
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.sandbox import execute_code_with_test, SandboxStatus


def validate_problem_definition(problem_data: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validates a problem JSON definition:
    1. Schema completeness.
    2. C_ref compiles and passes T_ref 100% in isolated execution.
    3. Provenance and cutoff timestamp documented.
    """
    required_fields = [
        "problem_id", "function_name", "docstring", "signature",
        "ref_implementation", "ref_test", "commit_hash", "commit_date"
    ]
    for field in required_fields:
        if field not in problem_data or not problem_data[field]:
            return False, f"Missing or empty required field: {field}"

    # Execution sanity check
    ref_code = problem_data["ref_implementation"]
    ref_test = problem_data["ref_test"]

    status, output, elapsed, backend = execute_code_with_test(ref_code, ref_test, timeout_seconds=5.0)
    if status != SandboxStatus.PASSED:
        return False, f"C_ref failed on T_ref ({status}): {output}"

    return True, f"Valid (passed T_ref in {elapsed:.1f}ms using {backend})"


if __name__ == "__main__":
    template_path = Path("e:/paper2/data/template_problem.json")
    if template_path.exists():
        data = json.loads(template_path.read_text(encoding="utf-8"))
        is_valid, msg = validate_problem_definition(data)
        print(f"Template validation result: {is_valid} -> {msg}")
