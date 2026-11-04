def test_empty_graph():
    assert detect_dag_cycle_and_ancestors([], []) == (False, {})

def test_no_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not cycle
    assert ancestors == {
        'A': set(),
        'B': {'A'},
        'C': {'A', 'B'}
    }

def test_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert cycle
    assert ancestors == {
        'A': set(),
        'B': {'A'},
        'C': {'A', 'B'}
    }

def test_single_node():
    nodes = ['A']
    edges = []
    cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not cycle
    assert ancestors == {'A': set()}

def test_invalid_input():
    try:
        detect_dag_cycle_and_ancestors(None, None)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_unreachable_nodes():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B')]
    cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert not cycle
    assert ancestors == {
        'A': set(),
        'B': {'A'},
        'C': set()
    }