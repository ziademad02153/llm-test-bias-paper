def test_detect_dag_cycle_and_ancestors():
    # Test with a simple DAG (no cycle)
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

def test_detect_dag_cycle_and_ancestors_self_loop():
    # Test with a self-loop
    nodes = ['A']
    edges = [('A', 'A')]
    expected = (True, {'A': {'A'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected

def test_detect_dag_cycle_and_ancestors_large_graph():
    # Test with a larger graph to ensure correctness
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')]
    expected = (True, {'A': {'A', 'B', 'C', 'D', 'E', 'F'}, 'B': {'A', 'B', 'C', 'D', 'E', 'F'}, 
                     'C': {'A', 'B', 'C', 'D', 'E', 'F'}, 'D': {'A', 'B', 'C', 'D', 'E', 'F'}, 
                     'E': {'A', 'B', 'C', 'D', 'E', 'F'}, 'F': {'A', 'B', 'C', 'D', 'E', 'F'}})
    assert detect_dag_cycle_and_ancestors(nodes, edges) == expected
```

This suite of tests covers various scenarios including simple DAGs, graphs with cycles, empty inputs, a single node, self-loops, and a larger graph. Each test function asserts the expected behavior of the `detect_dag_cycle_and_ancestors` function based on its specification.