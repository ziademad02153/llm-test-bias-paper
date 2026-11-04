def test_detect_dag_cycle_and_ancestors():
    # Test case with no cycles and a simple DAG
    assert detect_dag_cycle_and_ancestors(["A", "B", "C"], [("A", "B"), ("B", "C")]) == (True, {"A": frozenset(), "B": frozenset({"A"}), "C": frozenset({"A", "B"})})

    # Test case with a cycle
    assert detect_dag_cycle_and_ancestors(["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "A")]) == (False, {"A": frozenset(), "B": frozenset({"A"}), "C": frozenset({"A", "B"})})

    # Test case with multiple nodes and cycles
    assert detect_dag_cycle_and_ancestors(["A", "B", "C", "D"], [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]) == (False, {"A": frozenset(), "B": frozenset({"A"}), "C": frozenset({"A", "B"}), "D": frozenset({"A", "B", "C"})})

    # Test case with a single node
    assert detect_dag_cycle_and_ancestors(["A"], []) == (True, {"A": frozenset()})

    # Test case with an empty graph
    assert detect_dag_cycle_and_ancestors([], []) == (True, {})

    # Test case with a complex DAG
    assert detect_dag_cycle_and_ancestors(["A", "B", "C", "D", "E"], [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "B")]) == (False, {"A": frozenset(), "B": frozenset({"A"}), "C": frozenset({"A", "B"}), "D": frozenset({"A", "B", "C"}), "E": frozenset({"A", "B", "C", "D"})})

test_detect_dag_cycle_and_ancestors()
```

This suite of tests covers various scenarios including graphs with no cycles, graphs with cycles, graphs with a single node, an empty graph, and a more complex DAG. Each test case uses `assert` statements to verify the correctness of the function under different conditions.