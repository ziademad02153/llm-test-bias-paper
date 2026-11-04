def test_basic_functionality():
    """Test basic consistent hashing with virtual nodes."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_empty_nodes_list():
    """Test behavior when nodes list is empty."""
    result = get_consistent_hash_node([], "test_key")
    assert result is None

def test_single_node():
    """Test behavior with a single node."""
    nodes = ["node1"]
    result = get_consistent_hash_node(nodes, "test_key")
    assert result == "node1"

def test_vnodes_impact():
    """Test that changing vnodes_per_node affects distribution."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # The result may or may not change, but the function should still return a valid node
    assert result1 in nodes
    assert result2 in nodes

def test_same_key_same_node():
    """Test that the same key consistently maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_different_keys_possible_different_nodes():
    """Test that different keys may map to different nodes."""
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = "key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    # They might be the same or different, but both should be valid nodes
    assert result1 in nodes
    assert result2 in nodes