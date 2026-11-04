from detect_dag_cycle_and_ancestors import detect_dag_cycle_and_ancestors

def test_empty_graph():
    assert detect_dag_cycle_and_ancestors([], []) == (True, {})

def test_simple_dag():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True
    assert ancestors == {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})}

def test_dag_with_no_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})}

def test_single_node_with_self_edge():
    nodes = ['A']
    edges = [('A', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True
    assert ancestors == {'A': frozenset({'A'})}

def test_disconnected_nodes():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset()}

def test_invalid_input():
    try:
        detect_dag_cycle_and_ancestors(None, None)
        assert False, "Expected TypeError"
    except TypeError:
        pass