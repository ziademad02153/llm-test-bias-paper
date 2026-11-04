def test_detect_dag_cycle_and_ancestors():
    # Test case 1: Simple DAG with no cycles
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})})

# Test case 2: Cycle detected
nodes = ['A', 'B', 'C']
edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'})})

# Test case 3: Single node graph
nodes = ['A']
edges = []
assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset()})

# Test case 4: Graph with multiple disconnected components
nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('C', 'D')]
assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset(), 'D': frozenset({'C'})})

# Test case 5: Graph with a cycle in one component and a valid DAG in another
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E')]
assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset({'A', 'B'}), 'D': frozenset(), 'E': frozenset({'D'})})

# Test case 6: Empty inputs
nodes = []
edges = []
assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {})

test_detect_dag_cycle_and_ancestors()
```

This suite of tests covers various scenarios including simple DAGs, cycles, single-node graphs, disconnected components, and edge cases like empty inputs.