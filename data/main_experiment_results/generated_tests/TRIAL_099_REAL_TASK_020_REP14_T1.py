def test_detect_dag_cycle_and_ancestors():
    # Test case with no cycles and multiple nodes
    assert detect_dag_cycle_and_ancestors(["a", "b", "c"], [("a", "b"), ("b", "c")]) == (True, {"a": frozenset(), "b": frozenset({"a"}), "c": frozenset({"a", "b"})})

    # Test case with a cycle
    assert detect_dag_cycle_and_ancestors(["a", "b", "c"], [("a", "b"), ("b", "a")]) == (False, {"a": frozenset(), "b": frozenset({"a"}), "c": frozenset()})

    # Test case with a single node
    assert detect_dag_cycle_and_ancestors(["a"], []) == (True, {"a": frozenset()})

    # Test case with multiple disconnected components
    assert detect_dag_cycle_and_ancestors(["a", "b", "c"], []) == (True, {"a": frozenset(), "b": frozenset(), "c": frozenset()})

    # Test case with empty inputs
    assert detect_dag_cycle_and_ancestors([], []) == (True, {})

    # Test case with a complex graph
    assert detect_dag_cycle_and_ancestors(["a", "b", "c", "d"], [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")]) == (False, {"a": frozenset({"d", "c", "b"}), "b": frozenset({"d", "c"}), "c": frozenset({"d"}), "d": frozenset()})

test_detect_dag_cycle_and_ancestors()
```

This suite of tests covers various scenarios including graphs with cycles, no cycles, single nodes, disconnected components, and complex graphs. Each test case uses `assert` statements to verify the expected behavior of the function under different conditions.