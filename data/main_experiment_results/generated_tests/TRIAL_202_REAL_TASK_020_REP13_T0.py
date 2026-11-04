def test_detect_dag_cycle_and_ancestors():
    # Test with a simple DAG (no cycles)
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    expected = (False, {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_with_cycle():
    # Test with a graph that has a cycle
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    expected = (True, {'A': {'A'}, 'B': {'A', 'B'}, 'C': {'A', 'B', 'C'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_empty_inputs():
    # Test with empty inputs
    nodes = []
    edges = []
    expected = (False, {})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_single_node():
    # Test with a single node
    nodes = ['A']
    edges = []
    expected = (False, {'A': set()})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_self_loops():
    # Test with self-loops (should be considered as cycles)
    nodes = ['A']
    edges = [('A', 'A')]
    expected = (True, {'A': {'A'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_large_graph():
    # Test with a larger graph to ensure performance and correctness
    nodes = [f'N{i}' for i in range(10)]
    edges = [(f'N{i}', f'N{i+1}') for i in range(9)] + [('N8', 'N2')]
    expected = (True, {f'N{i}': set([f'N{j}' for j in range(i)]) for i in range(10)})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected
```

These tests cover various scenarios including detecting cycles, computing ancestors, handling empty inputs, single nodes, self-loops, and a larger graph.