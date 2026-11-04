def test_get_consistent_hash_node_standard_input():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) is not None

def test_get_consistent_hash_node_empty_nodes():
    nodes = []
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) is None

def test_get_consistent_hash_node_empty_key():
    nodes = ["node1", "node2", "node3"]
    key = ""
    assert get_consistent_hash_node(nodes, key) is not None

def test_get_consistent_hash_node_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key, vnodes_per_node=5) is not None

def test_get_consistent_hash_node_single_node():
    nodes = ["node1"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_get_consistent_hash_node_same_key_different_nodes():
    nodes1 = ["node1", "node2", "node3"]
    nodes2 = ["node4", "node5", "node6"]
    key = "example_key"
    assert get_consistent_hash_node(nodes1, key)!= get_consistent_hash_node(nodes2, key)