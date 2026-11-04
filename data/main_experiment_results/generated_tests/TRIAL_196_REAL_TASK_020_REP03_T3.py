def test_empty_graph():
    """Test with an empty graph."""
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {}

def test_no_cycle():
    """Test with a graph that does not contain a cycle."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}}

def test_with_cycle():
    """Test with a graph that contains a cycle."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}}

def test_single_node():
    """Test with a graph that contains a single node."""
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set()}

def test_single_edge():
    """Test with a graph that contains a single edge."""
    nodes = ['A', 'B']
    edges = [('A', 'B')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {'A': set(), 'B': {'A'}}

def test_invalid_input():
    """Test with invalid input (non-list nodes and edges)."""
    try:
        detect_dag_cycle_and_ancestors('nodes', 'edges')
        assert False, "Expected TypeError"
    except TypeError:
        pass