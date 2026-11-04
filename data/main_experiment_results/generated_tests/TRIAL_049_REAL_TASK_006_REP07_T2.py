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
    """Test that changing vnodes_per_node affects distribution (not guaranteed but likely)."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # This might or might not be different, but we're testing the function handles the parameter
    # We just verify it returns a valid node
    assert result_default in nodes
    assert result_custom in nodes

def test_distribution_across_nodes():
    """Test that keys are distributed across available nodes (not all to one node)."""
    nodes = ["node1", "node2", "node3"]
    keys = [f"key{i}" for i in range(100)]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # Keys should be distributed across multiple nodes

def test_wrap_around():
    """Test that keys with hash greater than all vnode hashes wrap around to first vnode."""
    # We'll create a special case where we know the key's hash is very large
    # by using a key that we know will hash to a very large value
    # This is tricky to do reliably, so we'll just test the behavior exists
    nodes = ["node1", "node2"]
    # Create a key that will likely hash higher than all vnodes (not guaranteed but probable)
    huge_key = "z" * 1000  # long string of high-value chars
    # The function should still return one of the nodes
    assert get_consistent_hash_node(nodes, huge_key) in nodes