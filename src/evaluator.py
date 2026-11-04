"""
Core evaluation logic applying pre-registered oracle validity and defect detection criteria
at both test-case (sliced) and test-suite granularity.
"""

import ast
import re
from typing import List, Tuple, Dict, Any, Optional
from src.sandbox import execute_code_with_test, SandboxStatus
from src.schema import TestOracleOutput, ExperimentalCondition


def clean_test_code(code_str: str, target_fn_name: Optional[str] = None) -> str:
    """
    Cleans raw model output by:
    1. Extracting python code from markdown fences (```python ... ```).
    2. Stripping trailing conversational notes, explanations, or usage blocks.
    3. Stripping conversational preambles before the first python code statement.
    4. Stripping any dummy stub or shadowing re-definition of the target function.
    """
    text = code_str.strip()
    
    # 1. Extract markdown code blocks (handles both closed and unclosed ```python blocks)
    m = re.search(r"```(?:python)?\s*\n(.*?)(?:\n```|\Z)", text, re.DOTALL | re.IGNORECASE)
    if m:
        text = m.group(1).strip()
    elif "```" in text:
        text = re.sub(r"^```(?:python)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\n```\s*$", "", text).strip()

    # 2. Cut off trailing notes/explanations
    clean_lines = []
    for line in text.splitlines():
        if re.match(r"^(Note|Explanation|Usage|Output|Running the test)s?:", line.strip(), re.IGNORECASE):
            break
        clean_lines.append(line)
    text = "\n".join(clean_lines).strip()

    # 3. Strip leading conversational preamble before first code statement
    lines = text.splitlines()
    first_code_idx = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(("import ", "from ", "def ", "class ", "assert ", "@", "#")):
            first_code_idx = i
            break
    if first_code_idx > 0:
        text = "\n".join(lines[first_code_idx:]).strip()

    # 4. Strip any dummy stub or re-definition of target_fn before parsing
    if target_fn_name:
        pattern = rf"^[ \t]*def\s+{target_fn_name}\s*\([^\)]*\)[^:]*:[^\n]*\n(?:[ \t]+[^\n]*\n|[ \t]*\n)*"
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    return text


def _is_unittest_main(node: ast.AST) -> bool:
    """Detects calls to unittest.main() to prevent premature script termination."""
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        func = node.value.func
        if isinstance(func, ast.Attribute) and func.attr == "main":
            return True
    if isinstance(node, ast.If):
        for sub in ast.walk(node):
            if isinstance(sub, ast.Attribute) and sub.attr == "main":
                return True
    return False


def _is_shadowing_import(node: ast.AST, target_fn_name: Optional[str] = None) -> bool:
    """Detects imports that try to load non-existent user/solution modules or import target_fn."""
    dummy_modules = {"your_module", "solution", "my_solution", "task", "code", "file", "exercise", "src", "main"}
    if isinstance(node, ast.ImportFrom):
        if node.module in dummy_modules:
            return True
        if target_fn_name and any(alias.name == target_fn_name for alias in node.names):
            return True
    if isinstance(node, ast.Import):
        if any(alias.name in dummy_modules for alias in node.names):
            return True
    return False


def split_test_suite_into_cases(test_suite_code: str, target_fn_name: Optional[str] = None) -> List[str]:
    """
    Parses a test suite into discrete test cases (either individual test functions,
    unittest methods, or standalone assertion statements).
    Ensures that re-definitions of the target function and unittest.main() triggers are stripped.
    """
    cleaned_code = clean_test_code(test_suite_code, target_fn_name=target_fn_name)
    try:
        tree = ast.parse(cleaned_code)
    except SyntaxError:
        return [cleaned_code] if cleaned_code else []

    # Filter out shadowing function stubs, bogus imports, and unittest.main calls
    filtered_body = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if target_fn_name and node.name == target_fn_name:
                continue
        if _is_shadowing_import(node, target_fn_name):
            continue
        if _is_unittest_main(node):
            continue
        filtered_body.append(node)
    tree.body = filtered_body

    # Extract top-level setup lines (imports, assignments, helper functions/classes)
    setup_nodes = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("test_"):
                setup_nodes.append(node)
        elif isinstance(node, ast.ClassDef):
            has_tests = any(isinstance(sub, ast.FunctionDef) and sub.name.startswith("test_") for sub in node.body)
            if not has_tests:
                setup_nodes.append(node)
        elif isinstance(node, ast.Assert):
            pass
        else:
            setup_nodes.append(node)

    setup_code = ast.unparse(ast.Module(body=setup_nodes, type_ignores=[])).strip()

    cases = []

    # 1. Standalone test functions (def test_...():)
    func_defs = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_")
    ]
    for fn in func_defs:
        fn_src = ast.unparse(fn)
        case_body = f"{setup_code}\n\n{fn_src}\n\n{fn.name}()" if setup_code else f"{fn_src}\n\n{fn.name}()"
        cases.append(case_body.strip())

    # 2. Unittest test classes (class Test...(unittest.TestCase):)
    class_defs = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    for cls_node in class_defs:
        class_src = ast.unparse(cls_node)
        for sub in cls_node.body:
            if isinstance(sub, ast.FunctionDef) and sub.name.startswith("test_"):
                unit_runner = f"""import unittest
import sys
import io

{setup_code}

{class_src}

suite = unittest.TestSuite()
suite.addTest({cls_node.name}('{sub.name}'))
runner = unittest.TextTestRunner(stream=io.StringIO())
result = runner.run(suite)
if not result.wasSuccessful():
    err_msg = ""
    if result.errors:
        err_msg = result.errors[0][1]
    elif result.failures:
        err_msg = result.failures[0][1]
    raise AssertionError(f"UnitTest Failed: {{err_msg}}")
"""
                cases.append(unit_runner.strip())

    # 3. Top-level assert statements
    assert_nodes = [node for node in tree.body if isinstance(node, ast.Assert)]
    for a_node in assert_nodes:
        a_src = ast.unparse(a_node)
        case_body = f"{setup_code}\n{a_src}" if setup_code else a_src
        cases.append(case_body.strip())

    if not cases:
        clean_full = ast.unparse(tree).strip()
        if clean_full:
            cases.append(clean_full)

    return cases if cases else [cleaned_code]


def evaluate_generated_test(
    problem_id: str,
    condition: ExperimentalCondition,
    model_name: str,
    ref_implementation: str,
    faulty_implementation: str,
    generated_test_code: str,
    prompt_tokens: int = 0,
    completion_tokens: int = 0,
    timeout_seconds: float = 6.0,
    target_fn_name: Optional[str] = None
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
    raw_cases = split_test_suite_into_cases(generated_test_code, target_fn_name=target_fn_name)
    total_cases = len(raw_cases)

    valid_cases: List[str] = []
    invalid_cases: List[Dict[str, Any]] = []
    total_time_ms = 0.0

    failure_breakdown = {
        "SYNTAX_ERROR": 0,
        "IMPORT_ERROR": 0,
        "EXPECTATION_FAILURE": 0,
        "RUNTIME_EXCEPTION": 0,
        "TIMEOUT": 0
    }

    # Step 1: Validate each test case on C_ref
    for case in raw_cases:
        st, out, elapsed, _ = execute_code_with_test(ref_implementation, case, timeout_seconds=timeout_seconds)
        total_time_ms += elapsed
        if st == SandboxStatus.PASSED:
            valid_cases.append(case)
        else:
            # Categorize the exact failure cause on C_ref
            if st == SandboxStatus.SYNTAX_ERROR:
                cat = "SYNTAX_ERROR"
            elif "ModuleNotFoundError" in out or "ImportError" in out:
                cat = "IMPORT_ERROR"
            elif st == SandboxStatus.FAILED_ASSERTION:
                cat = "EXPECTATION_FAILURE"
            elif st == SandboxStatus.TIMEOUT:
                cat = "TIMEOUT"
            else:
                cat = "RUNTIME_EXCEPTION"
            
            failure_breakdown[cat] += 1
            invalid_cases.append({
                "category": cat,
                "status": st,
                "output_snippet": out[-300:] if out else ""
            })

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
                "failure_breakdown": failure_breakdown,
                "invalid_cases": invalid_cases
            }
        )

    # Step 2: Defect Detection with Strict Verification
    # (a) Execute each valid test case individually against C_faulty.
    # This guarantees that defect detection is driven solely by individual test cases
    # that are verified to pass C_ref, eliminating any concatenation/state-leak artifacts.
    detecting_cases: List[Dict[str, Any]] = []
    first_detection_output = ""
    backend = "unknown"

    for case in valid_cases:
        c_st, c_out, c_elapsed, bk = execute_code_with_test(
            faulty_implementation,
            case,
            timeout_seconds=timeout_seconds
        )
        total_time_ms += c_elapsed
        backend = bk
        if c_st in (SandboxStatus.FAILED_ASSERTION, SandboxStatus.RUNTIME_EXCEPTION, SandboxStatus.TIMEOUT):
            detecting_cases.append({
                "status": c_st,
                "output_snippet": c_out[-300:] if c_out else ""
            })
            if not first_detection_output:
                first_detection_output = c_out[:500]

    detects_fault = (len(detecting_cases) >= 1)

    # (b) Combined Suite Sanity Check:
    # Execute the concatenated valid suite against C_ref to confirm multi-test composability.
    filtered_suite = "\n\n".join(valid_cases)
    ref_suite_st, ref_suite_out, ref_suite_elapsed, _ = execute_code_with_test(
        ref_implementation,
        filtered_suite,
        timeout_seconds=timeout_seconds
    )
    total_time_ms += ref_suite_elapsed
    suite_clean_on_ref = (ref_suite_st == SandboxStatus.PASSED)

    return TestOracleOutput(
        problem_id=problem_id,
        condition=condition,
        model_name=model_name,
        generated_test=generated_test_code,
        is_valid=True,
        detects_fault=detects_fault,
        validation_output=f"{valid_count}/{total_cases} tests valid on C_ref (combined_clean={suite_clean_on_ref})",
        detection_output=first_detection_output if detects_fault else "ALL_VALID_TESTS_PASSED_C_FAULTY",
        execution_time_ms=total_time_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        metadata={
            "total_cases": total_cases,
            "valid_cases": valid_count,
            "validity_rate": validity_rate,
            "is_strictly_valid": is_strictly_valid,
            "detecting_case_count": len(detecting_cases),
            "detecting_cases": detecting_cases,
            "suite_clean_on_ref": suite_clean_on_ref,
            "failure_breakdown": failure_breakdown,
            "invalid_cases": invalid_cases,
            "backend": backend
        }
    )
