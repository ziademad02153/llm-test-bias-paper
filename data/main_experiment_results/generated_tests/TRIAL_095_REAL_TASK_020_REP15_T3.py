def test_empty_inputs():
    """Test with empty inputs"""
    has_cycle, ancestors = detect_dag_cycle_and_ancestors([], [])
    assert not has_cycle
    assert ancestors == {}

def test_no_cycle():
    """Test with a DAG (no cycle)"""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {"A": set(), "B": {"A"}, "C": {"A", "B"}}

def test_with_cycle():
    """Test with a graph containing a cycle"""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {"A": set(), "B": {"A"}, "C": {"A", "B"}}

def test_single_node():
    """Test with a single node and no edges"""
    nodes = ["A"]
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {"A": set()}

def test_invalid_input():
    """Test with invalid input (non-string node)"""
    nodes = [1, "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    try:
        detect_dag_cycle_and_ancestors(nodes, edges)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_invalid_edge():
    """Test with invalid edge (non-string node)"""
    nodes = ["A", "B", "C"]
    edges = [(1, "B"), ("B", "C")]
    try:
        detect_dag_cycle_and_ancestors(nodes, edges)
        assert False, "Expected TypeError"
    except TypeError:
        pass