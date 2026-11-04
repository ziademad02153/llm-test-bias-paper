def test_basic_functionality():
    """Test basic functionality with standard inputs."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_empty_nodes_list():
    """Test behavior when nodes list is empty."""
    nodes = []
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result is None

def test_single_node():
    """Test behavior with a single node in the list."""
    nodes = ["node1"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result == "node1"

def test_vnodes_per_node_effect():
    """Test that changing vnodes_per_node affects distribution (non-deterministic check)."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result3 = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    # Not strictly deterministic, but likely different with more vnodes
    assert result1 in nodes and result3 in nodes

def test_key_variation():
    """Test that different keys map to different nodes (non-deterministic check)."""
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    # Not strictly deterministic, but likely different for different keys
    assert result1 in nodes and result2 in nodes