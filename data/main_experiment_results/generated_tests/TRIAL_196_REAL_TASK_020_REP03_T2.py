from detect_dag_cycle_and_ancestors import detect_dag_cycle_and_ancestors

def test_empty_graph():
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {}

def test_no_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A', 'B'})
    }

def test_with_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle
    assert ancestors == {
        'A': set(),
        'B': set(),
        'C': set()
    }

def test_single_node():
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset()
    }

def test_single_edge():
    nodes = ['A', 'B']
    edges = [('A', 'B')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'})
    }

def test_multiple_ancestors():
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'C'), ('B', 'C'), ('C', 'D')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not has_cycle
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset(),
        'C': frozenset({'A', 'B'}),
        'D': frozenset({'A', 'B', 'C'})
    }