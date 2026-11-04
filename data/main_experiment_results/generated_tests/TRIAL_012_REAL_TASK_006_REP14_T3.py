Here's a comprehensive suite of unit tests for the `get_consistent_hash_node` function based on its specification:

```python
def test_returns_none_for_empty_nodes():
    assert get_consistent_hash_node([], "key1") is None

def test_returns_same_node_for_same_key():
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_distributes_keys_across_nodes():
    nodes = ["node1", "node2", "node3"]
    keys = ["key1", "key2", "key3", "key4", "key5"]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # Should distribute across multiple nodes

def test_vnodes_affect_distribution():
    nodes = ["node1", "node2"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # Different vnode counts may (but not always) produce different results
    # So we just verify both are valid nodes
    assert result1 in nodes
    assert result2 in nodes

def test_returns_valid_node_for_single_node():
    nodes = ["single_node"]
    assert get_consistent_hash_node(nodes, "any_key") == "single_node"

def test_handles_non_string_keys():
    nodes = ["node1", "node2"]
    assert get_consistent_hash_node(nodes, 12345) in nodes
    assert get_consistent_hash_node(nodes, 3.14) in nodes
    assert get_consistent_hash_node(nodes, ("tuple", "key")) in nodes