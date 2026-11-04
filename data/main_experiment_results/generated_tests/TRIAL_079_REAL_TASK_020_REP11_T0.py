def test_detect_dag_cycle_and_ancestors():
    # Test with a simple DAG (no cycle)
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    expected = (False, {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_with_cycle():
    # Test with a graph that contains a cycle
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    expected = (True, {'A': {'A', 'B', 'C'}, 'B': {'A', 'B', 'C'}, 'C': {'A', 'B', 'C'}})
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

def test_detect_dag_cycle_and_ancestors_self_loop():
    # Test with a self-loop
    nodes = ['A']
    edges = [('A', 'A')]
    expected = (True, {'A': {'A'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_large_graph():
    # Test with a larger graph to check performance and correctness
    nodes = [f'N{i}' for i in range(10)]
    edges = [(f'N{i}', f'N{i+1}') for i in range(9)]
    expected = (False, {nodes[i]: set(nodes[:i]) for i in range(len(nodes))})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected
```

These tests cover various scenarios including detecting cycles, handling different graph structures, and edge cases such as empty inputs and self-loops.