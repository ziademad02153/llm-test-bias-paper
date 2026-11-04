def test_detect_dag_cycle_and_ancestors():
    # Test with a simple DAG (no cycle)
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C')]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (False, {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}})

def test_detect_dag_cycle_and_ancestors_with_cycle():
    # Test with a graph that has a cycle
    nodes = ['A', 'B', 'C']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (True, {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}})

def test_detect_dag_cycle_and_ancestors_empty_inputs():
    # Test with empty nodes and edges
    nodes = []
    edges = []
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (False, {})

def test_detect_dag_cycle_and_ancestors_single_node():
    # Test with a single node
    nodes = ['A']
    edges = []
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (False, {'A': set()})

def test_detect_dag_cycle_and_ancestors_self_loop():
    # Test with a self-loop
    nodes = ['A']
    edges = [('A', 'A')]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (True, {'A': set()})

def test_detect_dag_cycle_and_ancestors_large_graph():
    # Test with a larger graph to check performance and correctness
    nodes = [f'Node{i}' for i in range(10)]
    edges = [(f'Node{i}', f'Node{i+1}') for i in range(9)] + [('Node8', 'Node0')]
    result = detect_dag_cycle_and_ancestors(nodes, edges)
    assert result == (True, {nodes[i]: set(nodes[:i]) for i in range(len(nodes))})

test_detect_dag_cycle_and_ancestors()
test_detect_dag_cycle_and_ancestors_with_cycle()
test_detect_dag_cycle_and_ancestors_empty_inputs()
test_detect_dag_cycle_and_ancestors_single_node()
test_detect_dag_cycle_and_ancestors_self_loop()
test_detect_dag_cycle_and_ancestors_large_graph()
```

This suite of tests covers various scenarios including a simple DAG, a graph with a cycle, empty inputs, a single node, a self-loop, and a larger graph. Each test function asserts the expected behavior based on the function's specification.