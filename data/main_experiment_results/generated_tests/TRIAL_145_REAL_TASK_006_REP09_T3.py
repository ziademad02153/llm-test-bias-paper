def test_returns_none_for_empty_nodes():
    """Test that None is returned when nodes list is empty."""
    assert get_consistent_hash_node([], "some_key") is None

def test_returns_same_node_for_same_key():
    """Test that the same node is returned for the same key consistently."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_distributes_keys_across_nodes():
    """Test that keys are distributed across available nodes (not all to one)."""
    nodes = ["node1", "node2", "node3"]
    keys = ["key1", "key2", "key3", "key4", "key5"]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # At least two different nodes should be used

def test_vnodes_per_node_affects_distribution():
    """Test that changing vnodes_per_node affects distribution."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # Not guaranteed to be different, but likely with high vnodes
    assert result_default != result_custom or len(nodes) == 1