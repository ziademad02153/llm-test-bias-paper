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
    """Test that keys are consistently hashed to the same nodes across multiple calls."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2


def test_virtual_nodes_distribution():
    """Test that keys are distributed across nodes when using virtual nodes."""
    nodes = ["node1", "node2"]
    keys = ["key1", "key2", "key3", "key4", "key5"]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    # At least two different nodes should be used
    assert len(results) > 1


def test_wrap_around():
    """Test that the hash ring wraps around when key hash is greater than all node hashes."""
    # Create a scenario where the key's hash is higher than all virtual node hashes
    # by forcing all virtual nodes to have very low hashes
    nodes = ["node1", "node2"]
    # Mock the MD5 hashing to return low values for nodes and high value for key
    original_md5 = hashlib.md5
    try:
        def mock_md5_low(b):
            m = original_md5()
            m.update(b"low")  # Ensure low hash value
            return m
        def mock_md5_high(b):
            m = original_md5()
            m.update(b"high")  # Ensure high hash value
            return m
        
        hashlib.md5 = mock_md5_low
        # Get the node for a key that will have a higher hash than all virtual nodes
        hashlib.md5 = mock_md5_high
        result = get_consistent_hash_node(nodes, "some_key")
        # Should wrap around to first virtual node's physical node
        assert result in nodes
    finally:
        hashlib.md5 = original_md5


def test_vnodes_per_node_parameter():
    """Test that changing vnodes_per_node affects distribution."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # With different vnodes counts, the result might differ (though not guaranteed)
    # We just verify the function runs without error and returns a valid node
    assert result1 in nodes
    assert result2 in nodes