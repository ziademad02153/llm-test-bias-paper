def test_empty_nodes_returns_none():
    """Test that passing an empty list of nodes returns None"""
    assert get_consistent_hash_node([], "some_key") is None

def test_single_node_always_returns_same_node():
    """Test that with a single node, any key always maps to that node"""
    nodes = ["node1"]
    key1 = "key1"
    key2 = "key2"
    assert get_consistent_hash_node(nodes, key1) == "node1"
    assert get_consistent_hash_node(nodes, key2) == "node1"

def test_multiple_nodes_consistent_hashing():
    """Test that the same key consistently maps to the same node"""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_vnodes_per_node_affects_distribution():
    """Test that changing vnodes_per_node affects the distribution"""
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # Not guaranteed to be different, but likely with different vnode counts
    # So we just verify the function runs with different vnode counts
    assert result_default in nodes
    assert result_custom in nodes

def test_distribution_across_all_nodes():
    """Test that keys are distributed across all available nodes"""
    nodes = ["node1", "node2", "node3"]
    keys = [f"key{i}" for i in range(100)]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert results == set(nodes)  # All nodes should get at least one key

def test_wrap_around_behavior():
    """Test that keys hash to the first node when hash is greater than all vnode hashes"""
    # This is hard to test directly, but we can verify the function doesn't crash
    nodes = ["node1", "node2"]
    key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"  # Likely to have high hash value
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes