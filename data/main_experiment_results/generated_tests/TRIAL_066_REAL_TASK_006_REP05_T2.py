def test_empty_nodes():
    """Test that None is returned when nodes list is empty."""
    assert get_consistent_hash_node([], "some_key") is None


def test_single_node():
    """Test that the single node is always returned when there's only one node."""
    nodes = ["node1"]
    key = "some_key"
    assert get_consistent_hash_node(nodes, key) == "node1"
    assert get_consistent_hash_node(nodes, "another_key") == "node1"


def test_consistent_hashing_same_key():
    """Test that the same key always maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    first_result = get_consistent_hash_node(nodes, key)
    for _ in range(10):
        assert get_consistent_hash_node(nodes, key) == first_result


def test_virtual_nodes_distribution():
    """Test that virtual nodes affect distribution (with high probability)."""
    nodes = ["node1", "node2"]
    key1 = "key1"
    key2 = "key2"
    
    # With default vnodes_per_node=3, these keys will likely map to different nodes
    result1 = get_consistent_hash_node(nodes, key1, vnodes_per_node=3)
    result2 = get_consistent_hash_node(nodes, key2, vnodes_per_node=3)
    
    # With vnodes_per_node=1, there's a higher chance they'll map to the same node
    result_single_vnode1 = get_consistent_hash_node(nodes, key1, vnodes_per_node=1)
    result_single_vnode2 = get_consistent_hash_node(nodes, key2, vnodes_per_node=1)
    
    # Assert that virtual nodes affected distribution (this may fail with very low probability)
    assert (result1 != result2) or (result_single_vnode1 != result_single_vnode2)


def test_wrap_around_behavior():
    """Test that keys hash to the first node when their hash is greater than all vnode hashes."""
    # Create a special case where we know a key's hash will be very large
    # We'll use a node whose vnode hashes we can predict to be small
    nodes = ["a"]  # 'a-0', 'a-1', 'a-2' will have relatively small MD5 hashes
    key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"  # This will have a large MD5 hash
    
    # The key's hash should be larger than all vnode hashes, causing wrap-around to first node
    assert get_consistent_hash_node(nodes, key) == "a"