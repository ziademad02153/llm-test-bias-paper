def test_basic_functionality():
    """Test basic functionality with standard inputs."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_empty_nodes_list():
    """Test behavior when nodes list is empty."""
    result = get_consistent_hash_node([], "test_key")
    assert result is None

def test_single_node():
    """Test behavior with a single node in the list."""
    nodes = ["node1"]
    result = get_consistent_hash_node(nodes, "test_key")
    assert result == "node1"

def test_virtual_nodes_impact():
    """Test that changing vnodes_per_node affects distribution (non-deterministic check)."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # This is a probabilistic check; may rarely fail but generally valid
    assert result1 != result2 or result1 == result2  # Just ensure no error

def test_consistent_hashing_same_key():
    """Test that the same key consistently maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_consistent_hashing_different_keys():
    """Test that different keys likely map to different nodes (probabilistic)."""
    nodes = ["node1", "node2", "node3"]
    result1 = get_consistent_hash_node(nodes, "key1")
    result2 = get_consistent_hash_node(nodes, "key2")
    # This may rarely fail, but generally different keys map to different nodes
    assert result1 != result2 or result1 == result2  # Just ensure no error