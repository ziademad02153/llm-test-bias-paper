import detect_dag_cycle_and_ancestors

def test_empty_graph():
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {}

def test_simple_dag():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A', 'B'})
    }

def test_cyclic_graph():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A', 'B'})
    }

def test_disconnected_graph():
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('C', 'D')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset(),
        'D': frozenset({'C'})
    }

def test_single_node_graph():
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset()
    }

def test_self_loop():
    nodes = ['A']
    edges = [('A', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {
        'A': frozenset()
    }