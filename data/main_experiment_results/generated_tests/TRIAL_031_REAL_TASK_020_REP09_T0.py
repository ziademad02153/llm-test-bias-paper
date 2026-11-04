def test_detect_dag_cycle_and_ancestors():
    # Test with a simple DAG (Directed Acyclic Graph)
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    expected = (False, {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_with_cycle():
    # Test with a graph that contains a cycle
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    expected = (True, {'A': {'A'}, 'B': {'A', 'B'}, 'C': {'A', 'B', 'C'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_empty_nodes():
    # Test with empty nodes list
    nodes = []
    edges = []
    expected = (False, {})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_empty_edges():
    # Test with non-empty nodes and empty edges
    nodes = ['A', 'B', 'C']
    edges = []
    expected = (False, {'A': set(), 'B': set(), 'C': set()})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_single_node():
    # Test with a single node
    nodes = ['A']
    edges = []
    expected = (False, {'A': set()})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_self_loop():
    # Test with a self-loop edge
    nodes = ['A']
    edges = [('A', 'A')]
    expected = (True, {'A': {'A'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected
```

These tests cover various scenarios including a simple DAG, a graph with a cycle, empty inputs, a single node, and a self-loop. Each test function asserts the expected behavior of the `detect_dag_cycle_and_ancestors` function based on its specification.