from detect_dag_cycle_and_ancestors import detect_dag_cycle_and_ancestors

def test_empty_graph():
    """Test an empty graph with no nodes and edges."""
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {}

def test_no_cycle():
    """Test a graph with no cycles."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is False
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A', 'B'})
    }

def test_cycle():
    """Test a graph with a cycle."""
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {
        'A': set(),
        'B': set(),
        'C': set()
    }

def test_disconnected_nodes():
    """Test a graph with disconnected nodes."""
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('C', 'D')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is False
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset(),
        'D': frozenset({'C'})
    }

def test_self_loop():
    """Test a graph with a self-loop."""
    nodes = ['A']
    edges = [('A', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle is True
    assert ancestors == {
        'A': set()
    }