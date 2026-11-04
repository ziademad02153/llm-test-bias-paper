import pytest

def test_empty_graph():
    nodes = []
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True
    assert ancestors == {}

def test_single_node_no_cycle():
    nodes = ['A']
    edges = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset()}

def test_multiple_nodes_no_cycle():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})}

def test_cycle_detection():
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True

def test_invalid_input():
    nodes = None
    edges = None
    with pytest.raises(TypeError):
        detect_dag_cycle_and_ancestors(nodes, edges)

def test_ancestors_computation():
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A'}), 'D': frozenset({'A', 'B', 'C'})}