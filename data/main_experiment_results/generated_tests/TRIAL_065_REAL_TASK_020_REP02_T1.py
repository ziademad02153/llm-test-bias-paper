def test_detect_dag_cycle_and_ancestors():
    # Test case with a simple DAG (no cycle)
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})})

def test_detect_dag_cycle_and_ancestors_with_cycle():
    # Test case with a cycle
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {})

def test_detect_dag_cycle_and_ancestors_empty_inputs():
    # Test case with empty inputs
    nodes = []
    edges = []
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {})

def test_detect_dag_cycle_and_ancestors_single_node():
    # Test case with a single node
    nodes = ['A']
    edges = []
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset()})

def test_detect_dag_cycle_and_ancestors_complex_graph():
    # Test case with a more complex graph
    nodes = ['A', 'B', 'C', 'D', 'E']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A'}), 'D': frozenset({'A', 'B', 'C'}), 'E': frozenset({'A', 'B', 'C', 'D'})})

def test_detect_dag_cycle_and_ancestors_self_loop():
    # Test case with a self-loop
    nodes = ['A']
    edges = [('A', 'A')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {})
```

These tests cover various scenarios including simple DAGs, cycles, empty inputs, single nodes, and more complex graphs. Each test checks the function's ability to correctly identify cycles and compute ancestors for each node.