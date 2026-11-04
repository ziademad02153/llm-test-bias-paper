def test_basic_functionality():
    """Test basic consistent hashing with virtual nodes."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes  # Should return one of the nodes

def test_empty_nodes_list():
    """Test behavior when nodes list is empty."""
    result = get_consistent_hash_node([], "test_key")
    assert result is None  # Should return None for empty nodes list

def test_single_node():
    """Test behavior with a single node in the list."""
    nodes = ["node1"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result == "node1"  # Should always return the single node

def test_vnodes_per_node_impact():
    """Test that changing vnodes_per_node affects distribution (non-deterministic check)."""
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = "key2"
    # With default vnodes_per_node=3
    result_default = get_consistent_hash_node(nodes, key1)
    # With higher vnodes_per_node
    result_high_vnodes = get_consistent_hash_node(nodes, key1, vnodes_per_node=100)
    # Not guaranteed, but very likely to differ with high vnodes
    assert result_default != result_high_vnodes or key1 == key2

def test_consistent_hashing_same_key():
    """Test that the same key consistently maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2  # Same key should yield same node

def test_key_variations():
    """Test that different keys likely map to different nodes (probabilistic)."""
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = "key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    assert result1 != result2 or key1 == key2  # Different keys likely map differently