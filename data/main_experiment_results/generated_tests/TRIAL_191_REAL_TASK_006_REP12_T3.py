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

def test_vnodes_per_node():
    """Test behavior with custom vnodes_per_node parameter."""
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=1)
    result3 = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    assert result1 in nodes and result3 in nodes

def test_key_distribution():
    """Test that keys are distributed across nodes (not all to one)."""
    nodes = ["node1", "node2", "node3"]
    keys = [f"key_{i}" for i in range(100)]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # Keys should map to multiple nodes

def test_consistent_hashing_same_key():
    """Test that the same key always maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2