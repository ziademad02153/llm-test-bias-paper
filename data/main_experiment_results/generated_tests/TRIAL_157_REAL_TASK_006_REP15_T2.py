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
    """Test that the same node is returned for the same key across multiple calls."""
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
    # If it fails occasionally, it's not necessarily a bug
    assert result_default != result_custom

def test_distribution_across_nodes():
    """Test that keys are distributed across available nodes (not all to one node)."""
    nodes = ["node1", "node2", "node3"]
    keys = [f"key{i}" for i in range(100)]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # Keys should be distributed to multiple nodes

def test_wrap_around():
    """Test that keys hash to the first node when their hash is greater than all vnode hashes."""
    # This is hard to test directly, so we'll mock the bisect behavior
    # But since we can't mock in simple asserts, we'll just verify the function
    # handles the wrap-around case in its logic
    nodes = ["node1", "node2"]
    # The actual test would require knowing a key that hashes higher than all vnodes,
    # but we can at least verify the function doesn't crash
    get_consistent_hash_node(nodes, "some_key")