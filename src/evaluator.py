"""
Core evaluation logic applying pre-registered oracle validity and defect detection criteria
at both test-case (sliced) and test-suite granularity.
"""

import ast
import re
from typing import List, Tuple, Dict, Any, Optional
from src.sandbox import execute_code_with_test, SandboxStatus
from src.schema import TestOracleOutput, ExperimentalCondition


def split_test_suite_into_cases(test_suite_code: str) -> List[str]:
    """
    Parses a test suite into discrete test cases (either individual test functions,
    or standalone assertion statements/blocks).
    """
    try:
        tree = ast.parse(test_suite_code)
    except SyntaxError:
        # If unparseable as AST, treat the whole code as one single case
        return [test_suite_code.strip()] if test_suite_code.strip() else []

    cases = []
    # Check if there are function definitions (e.g., def test_...():)
    func_defs = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    
    if func_defs:
        # Extract each function + immediate call to it
        for fn in func_defs:
            fn_code = ast.get_source_segment(test_suite_code, fn)
            call_code = f"{fn.name}()"
            cases.append(f"{fn_code}\n{call_code}")
    else:
        # Individual top-level statements/assertions
        lines = [line.strip() for line in test_suite_code.splitlines() if line.strip() and not line.strip().startswith("#")]
        if lines:
            # Group contiguous assertions or treat line by line
            for line in lines:
                if line.startswith("assert"):
                    cases.append(line)
        if not cases and test_suite_code.strip():
            cases.append(test_suite_code.strip())

    return cases if cases else [test_suite_code.strip()]


def evaluate_generated_test(
    problem_id: str,
    condition: ExperimentalCondition,
    model_name: str,
    ref_implementation: str,
    faulty_implementation: str,
    generated_test_code: str,
    prompt_tokens: int = 0,
    completion_tokens: int = 0,
    timeout_seconds: float = 6.0
) -> TestOracleOutput:
    """
    Evaluates a generated test suite applying pre-registered validity filtering:
    
    1. Test-Case Level Slicing:
       The suite is decomposed into individual test cases {t_1, ..., t_k}.
       Each t_j is executed on C_ref.
       t_j is VALID iff Execute(C_ref, t_j) == PASSED.
       T_valid = { t_j | t_j is VALID }.
       
    2. Validity Metrics:
       - total_test_cases = k
       - valid_test_cases = |T_valid|
       - validity_rate = |T_valid| / k
       - is_valid (usable suite) = (|T_valid| >= 1)
       - is_strictly_valid = (|T_valid| == k)
       
    3. Defect Detection:
       If is_valid is False (0 valid tests), detects_fault = False.
       Otherwise, execute T_valid against C_faulty.
       detects_fault = True iff Execute(C_faulty, T_valid) in (FAILED_ASSERTION, RUNTIME_EXCEPTION, TIMEOUT).
    """
    raw_cases = split_test_suite_into_cases(generated_test_code)
    total_cases = len(raw_cases)

    valid_cases: List[str] = []
    invalid_cases: List[str] = []
    total_time_ms = 0.0

    # Step 1: Validate each test case on C_ref
    for case in raw_cases:
        st, out, elapsed, _ = execute_code_with_test(ref_implementation, case, timeout_seconds=timeout_seconds)
        total_time_ms += elapsed
        if st == SandboxStatus.PASSED:
            valid_cases.append(case)
        else:
            invalid_cases.append(case)

    valid_count = len(valid_cases)
    validity_rate = (valid_count / total_cases) if total_cases > 0 else 0.0
    is_usable_valid = (valid_count >= 1)
    is_strictly_valid = (valid_count == total_cases and total_cases > 0)

    if not is_usable_valid:
        # Zero valid test cases generated (all failed on reference implementation)
        return TestOracleOutput(
            problem_id=problem_id,
            condition=condition,
            model_name=model_name,
            generated_test=generated_test_code,
            is_valid=False,
            detects_fault=False,
            validation_output=f"0/{total_cases} tests valid on C_ref",
            detection_output="SKIPPED_DUE_TO_ZERO_VALID_TESTS",
            execution_time_ms=total_time_ms,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            metadata={
                "total_cases": total_cases,
                "valid_cases": 0,
                "validity_rate": 0.0,
                "is_strictly_valid": False,
                "invalid_cases": invalid_cases
            }
        )

    # Step 2: Combine all valid test cases into a filtered suite and execute on C_faulty
    filtered_suite = "\n\n".join(valid_cases)
    det_status, det_output, det_elapsed, backend = execute_code_with_test(
        faulty_implementation,
        filtered_suite,
        timeout_seconds=timeout_seconds
    )
    total_time_ms += det_elapsed

    detects_fault = (det_status in (
        SandboxStatus.FAILED_ASSERTION,
        SandboxStatus.RUNTIME_EXCEPTION,
        SandboxStatus.TIMEOUT
    ))

    return TestOracleOutput(
        problem_id=problem_id,
        condition=condition,
        model_name=model_name,
        generated_test=filtered_suite,
        is_valid=True,
        detects_fault=detects_fault,
        validation_output=f"{valid_count}/{total_cases} test cases valid on C_ref ({validity_rate:.1%})",
        detection_output=f"{det_status}: {det_output}",
        execution_time_ms=total_time_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        metadata={
            "total_cases": total_cases,
            "valid_cases": valid_count,
            "validity_rate": validity_rate,
            "is_strictly_valid": is_strictly_valid,
            "invalid_cases": invalid_cases,
            "backend": backend
        }
    )
