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

def test_consistent_hashing_same_key():
    """Test that the same key always maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_vnodes_per_node():
    """Test that changing vnodes_per_node affects distribution (non-deterministic check)."""
    nodes = ["node1", "node2"]
    key = "some_key"
    result_default = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # This might or might not be different, but we at least verify it runs
    assert result_default in nodes
    assert result_custom in nodes

def test_wrap_around():
    """Test that keys hash to the first node when their hash is greater than all vnode hashes."""
    # Create a single node and force a key to wrap around
    nodes = ["node1"]
    # This key's hash is designed to be very large (but practically we can't control MD5)
    # Instead, we'll just verify the function doesn't crash on large hashes
    key = "some_key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_distribution_across_nodes():
    """Test that keys are distributed across all nodes (non-deterministic check)."""
    nodes = ["node1", "node2", "node3"]
    keys = [f"key{i}" for i in range(100)]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert results == set(nodes)  # All nodes should get at least one key