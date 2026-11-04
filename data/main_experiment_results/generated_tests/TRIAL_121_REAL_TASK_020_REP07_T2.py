from typing import List, Tuple

def test_empty_graph():
    """Test an empty graph with no nodes and edges."""
    nodes: List[str] = []
    edges: List[Tuple[str, str]] = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {}

def test_single_node_no_cycle():
    """Test a graph with a single node and no edges."""
    nodes: List[str] = ["A"]
    edges: List[Tuple[str, str]] = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is False
    assert ancestors == {"A": frozenset()}

def test_single_node_with_self_cycle():
    """Test a graph with a single node and a self-edge."""
    nodes: List[str] = ["A"]
    edges: List[Tuple[str, str]] = [("A", "A")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {"A": frozenset()}

def test_multiple_nodes_no_cycle():
    """Test a graph with multiple nodes and no cycles."""
    nodes: List[str] = ["A", "B", "C"]
    edges: List[Tuple[str, str]] = [("A", "B"), ("B", "C")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is False
    assert ancestors == {
        "A": frozenset(),
        "B": frozenset({"A"}),
        "C": frozenset({"A", "B"})
    }

def test_multiple_nodes_with_cycle():
    """Test a graph with multiple nodes and a cycle."""
    nodes: List[str] = ["A", "B", "C"]
    edges: List[Tuple[str, str]] = [("A", "B"), ("B", "C"), ("C", "A")]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {
        "A": frozenset(),
        "B": frozenset({"A"}),
        "C": frozenset({"A", "B"})
    }