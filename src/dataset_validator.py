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
    2. Temporal gate verification (commit_date >= 2025-07-01).
    3. C_ref compiles and passes T_ref 100% in isolated execution.
    4. 4-stage screening audit flags verified.
    """
    required_fields = [
        "problem_id", "function_name", "docstring", "signature",
        "ref_implementation", "ref_test", "commit_hash", "commit_date",
        "temporal_threshold", "screening_checks"
    ]
    for field in required_fields:
        if field not in problem_data or not problem_data[field]:
            return False, f"Missing or empty required field: {field}"

    # Verify temporal cutoff
    commit_date = problem_data.get("commit_date", "")
    if commit_date < "2025-07-01":
        return False, f"Temporal violation: commit_date ({commit_date}) is prior to cutoff 2025-07-01"

    # Verify screening flags
    checks = problem_data.get("screening_checks", {})
    required_checks = [
        "temporal_gate_pass", "net_new_provenance_pass",
        "pre_2024_clone_absence_pass", "ai_authorship_absence_pass",
        "standalone_functional_purity_pass"
    ]
    for chk in required_checks:
        if not checks.get(chk, False):
            return False, f"Screening check failed: {chk} is False or missing"

    # Execution sanity check
    ref_code = problem_data["ref_implementation"]
    ref_test = problem_data["ref_test"]

    status, output, elapsed, backend = execute_code_with_test(ref_code, ref_test, timeout_seconds=5.0)
    if status != SandboxStatus.PASSED:
        return False, f"C_ref failed on T_ref ({status}): {output}"

    return True, f"Valid (passed T_ref in {elapsed:.1f}ms using {backend})"


if __name__ == "__main__":
    problems_dir = Path("e:/paper2/data/problems")
    validated_count = 0
    total_count = 0

    # Validate template
    template_path = Path("e:/paper2/data/template_problem.json")
    if template_path.exists():
        data = json.loads(template_path.read_text(encoding="utf-8"))
        is_valid, msg = validate_problem_definition(data)
        print(f"[Template] {template_path.name}: {is_valid} -> {msg}")

    # Validate all problem files
    if problems_dir.exists():
        for prob_path in sorted(problems_dir.glob("*.json")):
            total_count += 1
            data = json.loads(prob_path.read_text(encoding="utf-8"))
            is_valid, msg = validate_problem_definition(data)
            print(f"[{data.get('problem_id', prob_path.stem)}] {prob_path.name}: {is_valid} -> {msg}")
            if is_valid:
                validated_count += 1

    print(f"\nTotal Problems Audited: {total_count}, Validated: {validated_count}/{total_count}")
