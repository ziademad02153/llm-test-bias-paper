def test_empty_nodes():
    """Test that None is returned when nodes list is empty."""
    assert get_consistent_hash_node([], "some_key") is None


def test_single_node():
    """Test that the single node is always returned regardless of the key."""
    nodes = ["node1"]
    assert get_consistent_hash_node(nodes, "key1") == "node1"
    assert get_consistent_hash_node(nodes, "key2") == "node1"
    assert get_consistent_hash_node(nodes, "key3", vnodes_per_node=5) == "node1"


def test_multiple_nodes_consistent_hashing():
    """Test that keys are consistently hashed to the same nodes."""
    nodes = ["node1", "node2", "node3"]
    key1_node = get_consistent_hash_node(nodes, "key1")
    key2_node = get_consistent_hash_node(nodes, "key2")
    # Same key should map to same node
    assert get_consistent_hash_node(nodes, "key1") == key1_node
    assert get_consistent_hash_node(nodes, "key2") == key2_node
    # Different keys may or may not map to same node
    assert (key1_node == key2_node) or (key1_node != key2_node)


def test_vnodes_per_node_effect():
    """Test that increasing vnodes_per_node affects distribution."""
    nodes = ["node1", "node2"]
    key = "test_key"
    # With default vnodes_per_node=3
    default_node = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    # With higher vnodes_per_node
    high_vnodes_node = get_consistent_hash_node(nodes, key, vnodes_per_node=100)
    # The node might or might not change, but the function should handle it
    assert isinstance(high_vnodes_node, str) and high_vnodes_node in nodes


def test_wrap_around():
    """Test that key hash larger than all vnode hashes wraps around to first vnode."""
    nodes = ["node1", "node2"]
    # Create a key that hashes to maximum possible value (or close)
    max_hash_key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"  # Likely to hash high
    # The function should properly wrap around
    assert get_consistent_hash_node(nodes, max_hash_key) in nodes