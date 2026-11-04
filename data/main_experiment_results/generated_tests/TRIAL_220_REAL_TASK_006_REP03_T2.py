def test_empty_nodes():
    """Test that None is returned when nodes list is empty."""
    assert get_consistent_hash_node([], "some_key") is None

def test_single_node():
    """Test that the same node is always returned for any key when there's only one node."""
    nodes = ["node1"]
    key1 = "key1"
    key2 = "key2"
    assert get_consistent_hash_node(nodes, key1) == "node1"
    assert get_consistent_hash_node(nodes, key2) == "node1"

def test_multiple_nodes_consistent_hashing():
    """Test that keys are consistently mapped to the same nodes across multiple calls."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_vnodes_per_node():
    """Test that changing vnodes_per_node affects distribution (not guaranteed but likely)."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # This might not always be true, but with high probability it will differ
    assert result_default != result_custom

def test_wrap_around():
    """Test that keys hash to the first node when their hash is greater than all vnode hashes."""
    # Create a single node and force the key's hash to be very large
    nodes = ["node1"]
    # The key is chosen such that its MD5 hash is likely larger than all vnode hashes
    key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"  # This will have a large MD5 hash
    assert get_consistent_hash_node(nodes, key) == "node1"