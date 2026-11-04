def test_empty_graph():
    """Test that an empty graph has no cycles and empty ancestor sets."""
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert all(not ancestors.get(node) for node in nodes)

def test_single_node_no_cycle():
    """Test that a graph with a single node and no edges has no cycles and empty ancestor sets."""
    nodes = ["A"]
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors["A"] == set()

def test_simple_dag():
    """Test that a simple DAG has no cycles and correct ancestor sets."""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors["A"] == set()
    assert ancestors["B"] == {"A"}
    assert ancestors["C"] == {"A", "B"}

def test_cycle_detection():
    """Test that a graph with a cycle is correctly detected."""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    has_cycle, _ = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle

def test_invalid_input():
    """Test that the function raises an error for invalid input."""
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "D")]  # Node "D" is not in the node list
    try:
        detect_dag_cycle_and_ancestors(nodes, edges)
        assert False, "Expected an error for invalid input"
    except ValueError:
        pass