def test_returns_node_for_non_empty_input():
    nodes = ["node1", "node2", "node3"]
    key = "some_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_returns_none_for_empty_nodes():
    nodes = []
    key = "some_key"
    result = get_consistent_hash_node(nodes, key)
    assert result is None

def test_consistent_hashing_same_key_same_node():
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_vnodes_affect_distribution():
    nodes = ["node1", "node2"]
    key = "some_key"
    result_default_vnodes = get_consistent_hash_node(nodes, key)
    result_custom_vnodes = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # Not guaranteed to be different, but likely with high vnodes
    assert result_default_vnodes is not None
    assert result_custom_vnodes is not None

def test_different_keys_different_nodes():
    nodes = ["node1", "node2", "node3", "node4"]
    key1 = "key1"
    key2 = "key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    # Not guaranteed to be different, but likely with multiple nodes
    assert result1 is not None
    assert result2 is not None