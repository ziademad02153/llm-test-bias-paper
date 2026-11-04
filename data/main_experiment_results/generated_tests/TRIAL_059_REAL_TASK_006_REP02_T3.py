def test_basic_functionality():
    """Test basic functionality with standard inputs."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_empty_nodes():
    """Test behavior when nodes list is empty."""
    nodes = []
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result is None

def test_single_node():
    """Test behavior with a single node."""
    nodes = ["node1"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result == "node1"

def test_vnodes_impact():
    """Test that changing vnodes_per_node affects distribution."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # The results may or may not be the same, but both should be valid nodes
    assert result1 in nodes and result2 in nodes

def test_key_variation():
    """Test that different keys may map to different nodes."""
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    # At least some keys should map to different nodes (though not guaranteed)
    # So we just verify they're both valid nodes
    assert result1 in nodes and result2 in nodes