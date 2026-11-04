def test_empty_inputs():
    """Test with empty inputs"""
    assert detect_dag_cycle_and_ancestors([], []) == (False, {})

def test_no_cycle():
    """Test with a DAG (no cycle)"""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {"A": set(), "B": {"A"}, "C": {"A", "B"}})

def test_with_cycle():
    """Test with a graph containing a cycle"""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {"A": set(), "B": {"A"}, "C": {"A", "B"}})

def test_single_node():
    """Test with a single node and no edges"""
    nodes = ["A"]
    edges = []
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {"A": set()})

def test_invalid_input():
    """Test with invalid input (non-string node)"""
    try:
        detect_dag_cycle_and_ancestors([1], [])
        assert False, "Expected TypeError"
    except TypeError:
        pass