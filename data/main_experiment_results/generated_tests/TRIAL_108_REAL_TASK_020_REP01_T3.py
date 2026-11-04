def test_detect_dag_cycle_and_ancestors_standard_input():
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not result[0]  # No cycle
    assert result[1] == {"A": set(), "B": {"A"}, "C": {"A", "B"}}

def test_detect_dag_cycle_and_ancestors_cycle_detection():
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result[0]  # Cycle detected

def test_detect_dag_cycle_and_ancestors_empty_input():
    nodes = []
    edges = []
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not result[0]  # No cycle
    assert result[1] == {}  # Empty ancestors dictionary

def test_detect_dag_cycle_and_ancestors_single_node():
    nodes = ["A"]
    edges = []
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not result[0]  # No cycle
    assert result[1] == {"A": set()}  # Single node with no ancestors

def test_detect_dag_cycle_and_ancestors_invalid_input():
    try:
        detect_dag_cycle_and_ancestors(None, None)
        assert False, "Expected TypeError"
    except TypeError:
        pass