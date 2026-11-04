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

    # Test case 4: Multiple disconnected components
    nodes = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('C', 'D')]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {'A': frozenset(), 'B': frozenset({'A'}), 'C': frozenset(), 'D': frozenset({'C'})})

    # Test case 5: Empty inputs
    nodes = []
    edges = []
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (True, {})

    # Test case 6: Large graph with cycles and ancestors
    nodes = [str(i) for i in range(10)]
    edges = [(str(i), str(i+1)) for i in range(9)] + [(str(8), str(0))]
    assert detect_dag_cycle_and_ancestors(nodes, edges) == (False, {str(i): frozenset({str(j) for j in range(i)}) for i in range(10)})

test_detect_dag_cycle_and_ancestors()
```

This suite of tests covers various scenarios including simple DAGs, graphs with cycles, single-node graphs, multiple disconnected components, empty inputs, and a larger graph to ensure the function behaves as expected across different conditions.