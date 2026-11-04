from typing import Tuple, Dict, Set

def test_empty_graph():
    nodes: list[str] = []
    edges: list[tuple[str, str]] = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True
    assert ancestors == {}

def test_simple_dag():
    nodes: list[str] = ['A', 'B', 'C']
    edges: list[tuple[str, str]] = [('A', 'B'), ('A', 'C')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    expected_ancestors: Dict[str, Set[str]] = {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A'})
    }
    assert ancestors == expected_ancestors

def test_graph_with_cycle():
    nodes: list[str] = ['A', 'B', 'C']
    edges: list[tuple[str, str]] = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == True
    assert ancestors == {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset({'A', 'B'})
    }

def test_single_node_graph():
    nodes: list[str] = ['A']
    edges: list[tuple[str, str]] = []
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    assert ancestors == {'A': frozenset()}

def test_disconnected_graph():
    nodes: list[str] = ['A', 'B', 'C', 'D']
    edges: list[tuple[str, str]] = [('A', 'B'), ('C', 'D')]
    has_cycle, ancestors = detect_dag_cycle_and_ancestors(nodes, edges)
    assert has_cycle == False
    expected_ancestors: Dict[str, Set[str]] = {
        'A': frozenset(),
        'B': frozenset({'A'}),
        'C': frozenset(),
        'D': frozenset({'C'})
    }
    assert ancestors == expected_ancestors

def test_invalid_input():
    try:
        detect_dag_cycle_and_ancestors(None, None)
        assert False, "Expected TypeError"
    except TypeError:
        assert True