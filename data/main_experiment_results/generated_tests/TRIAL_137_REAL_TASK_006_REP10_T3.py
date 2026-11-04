def test_basic_functionality():
    """Test basic functionality with standard inputs."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_empty_nodes():
    """Test behavior when nodes list is empty."""
    result = get_consistent_hash_node([], "test_key")
    assert result is None

def test_single_node():
    """Test behavior with a single node in the list."""
    nodes = ["node1"]
    key = "test_key"
    result = get_consistent_hash_node(nodes, key)
    assert result == "node1"

def test_vnodes_per_node():
    """Test behavior with custom vnodes_per_node."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result3 = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    assert result1 in nodes and result3 in nodes

def test_consistent_hashing_same_key():
    """Test that the same key consistently maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_consistent_hashing_different_keys():
    """Test that different keys may map to different nodes."""
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    # This may occasionally fail due to hash collision, but very unlikely
    assert result1 != result2 or len(nodes) == 1