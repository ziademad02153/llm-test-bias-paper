import ast
import json
import re
from pathlib import Path
import sys
from typing import Tuple, List, Dict, Any

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.sandbox import execute_code_with_test, SandboxStatus


class AssertRewriter(ast.NodeTransformer):
    def __init__(self):
        self.count = 0
        self.stmts = []

    def visit_Assert(self, node):
        idx = self.count
        self.count += 1
        stmt_src = ast.unparse(node)
        self.stmts.append(stmt_src)
        try_node = ast.parse(f'''
try:
    pass
    _assert_results.append({{'idx': {idx}, 'stmt': {repr(stmt_src)}, 'status': 'PASS'}})
except AssertionError:
    _assert_results.append({{'idx': {idx}, 'stmt': {repr(stmt_src)}, 'status': 'FAIL_ASSERT'}})
except Exception as _e:
    _assert_results.append({{'idx': {idx}, 'stmt': {repr(stmt_src)}, 'status': f'ERR:{{type(_e).__name__}}'}})
''').body[0]
        try_node.body[0] = node
        return try_node


def prepare_instrumented_test(test_code: str) -> Tuple[str, int]:
    tree = ast.parse(test_code)
    rewriter = AssertRewriter()
    new_tree = rewriter.visit(tree)
    ast.fix_missing_locations(new_tree)
    
    # Check which test functions exist
    test_funcs = [
        n.name for n in ast.walk(new_tree)
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
    ]
    
    # Check if they are already invoked at top-level
    invoked_calls = set()
    for n in new_tree.body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            if isinstance(n.value.func, ast.Name):
                invoked_calls.add(n.value.func.id)
                
    calls_to_append = [f"{fn}()" for fn in test_funcs if fn not in invoked_calls]
    
    inst_code = ast.unparse(new_tree)
    if calls_to_append:
        inst_code += "\n\n" + "\n".join(calls_to_append)
        
    return inst_code, rewriter.count


def verify_all_problems():
    problems = sorted((project_root / "data" / "problems").glob("REAL_TASK_*.json"))
    all_ok = True
    print(f"Verifying AST assertion slicing on {len(problems)} tasks...")

    for p_path in problems:
        p = json.loads(p_path.read_text(encoding="utf-8"))
        prob_id = p["problem_id"]
        fn_name = p["function_name"]

        inst_test, assert_count = prepare_instrumented_test(p["ref_test"])

        full_script = f"""import json
_assert_results = []
{p['ref_implementation']}
{inst_test}
print('ASSERT_JSON_OUTPUT:' + json.dumps(_assert_results))
"""
        st, out, el, be = execute_code_with_test(full_script, "")
        m = re.search(r"ASSERT_JSON_OUTPUT:(.+)", out)
        if not m:
            print(f"  [FAIL] {prob_id} ({fn_name}): Failed to parse JSON output! Status: {st}\nOutput: {out[:200]}")
            all_ok = False
            continue

        results = json.loads(m.group(1))
        passed = sum(1 for r in results if r["status"] == "PASS")
        total = len(results)
        if passed != total or total == 0:
            print(f"  [FAIL] {prob_id} ({fn_name}): {passed}/{total} Passed (Expected {assert_count})")
            all_ok = False
        else:
            print(f"  [OK] {prob_id} ({fn_name}): {passed}/{total} Passed (100% OK)")

    print("\nOVERALL VERIFICATION:", "ALL PASS 100%" if all_ok else "FAILED")
    return all_ok


if __name__ == "__main__":
    verify_all_problems()
