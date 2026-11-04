def test_empty_graph():
    """Test with an empty graph."""
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert all(not ancestors.get(node) for node in nodes)

def test_no_cycle():
    """Test with a graph that has no cycles."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors['A'] == set()
    assert ancestors['B'] == {'A'}
    assert ancestors['C'] == {'A', 'B'}

def test_with_cycle():
    """Test with a graph that has a cycle."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors['A'] == {'C'}
    assert ancestors['B'] == {'A'}
    assert ancestors['C'] == {'A', 'B'}

def test_single_node():
    """Test with a graph that has a single node and no edges."""
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors['A'] == set()

def test_single_edge():
    """Test with a graph that has two nodes and a single edge."""
    nodes = ['A', 'B']
    edges = [('A', 'B')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors['A'] == set()
    assert ancestors['B'] == {'A'}

def test_invalid_input():
    """Test with invalid input (node not in nodes list)."""
    nodes = ['A', 'B']
    edges = [('A', 'C')]
    try:
        detect_dag_cycle_and_ancestors(nodes, edges)
        assert False, "Expected ValueError"
    except ValueError:
        pass