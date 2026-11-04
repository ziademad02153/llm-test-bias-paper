def test_empty_graph():
    """Test an empty graph with no nodes and edges."""
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {}

def test_no_cycle():
    """Test a graph with no cycles."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}}

def test_with_cycle():
    """Test a graph with a cycle."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}}

def test_single_node():
    """Test a graph with a single node and no edges."""
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set()}

def test_invalid_input():
    """Test the function with invalid input (non-list nodes and edges)."""
    try:
        detect_dag_cycle_and_ancestors('A', [('A', 'B')])
        assert False, "Expected a TypeError"
    except TypeError:
        pass

def test_unreachable_nodes():
    """Test a graph with unreachable nodes."""
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}, 'D': set()}