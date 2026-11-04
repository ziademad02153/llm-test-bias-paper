def test_empty_nodes_returns_none():
    assert get_consistent_hash_node([], "some_key") is None

def test_single_node_always_returns_same_node():
    nodes = ["node1"]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) == "node1"
    assert get_consistent_hash_node(nodes, "another_key") == "node1"

def test_multiple_nodes_consistent_hashing():
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = "key2"
    # Same key should always map to same node
    assert get_consistent_hash_node(nodes, key1) == get_consistent_hash_node(nodes, key1)
    # Different keys may map to same or different nodes
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    assert result1 in nodes
    assert result2 in nodes

def test_virtual_nodes_distribution():
    nodes = ["nodeA", "nodeB"]
    # With default 3 vnodes, we should see distribution between both nodes
    results = {get_consistent_hash_node(nodes, f"key{i}") for i in range(100)}
    assert results == {"nodeA", "nodeB"}

def test_custom_vnodes_per_node():
    nodes = ["nodeX", "nodeY"]
    # With 1 vnode, distribution might be less balanced
    results = [get_consistent_hash_node(nodes, f"key{i}", 1) for i in range(100)]
    assert all(node in nodes for node in results)
    # With high vnodes, should still work
    high_vnodes_result = get_consistent_hash_node(nodes, "some_key", 1000)
    assert high_vnodes_result in nodes

def test_key_hash_wraparound():
    nodes = ["node1"]
    # Force a wrap-around case by using a key that hashes higher than all vnodes
    # Since we can't predict actual hashes, we test that it still returns a node
    assert get_consistent_hash_node(nodes, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "node1"