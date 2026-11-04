def test_returns_none_for_empty_nodes():
    assert get_consistent_hash_node([], "key1") is None

def test_returns_same_node_for_same_key():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2

def test_distributes_keys_across_nodes():
    nodes = ["node1", "node2", "node3"]
    keys = ["key1", "key2", "key3", "key4", "key5"]
    results = {get_consistent_hash_node(nodes, key) for key in keys}
    assert len(results) > 1  # Keys should distribute across multiple nodes

def test_vnodes_affect_distribution():
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key)
    result_vnodes = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # With high probability, different vnodes should give different results
    assert result_default != result_vnodes

def test_handles_single_node():
    nodes = ["node1"]
    assert get_consistent_hash_node(nodes, "key1") == "node1"