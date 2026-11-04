def test_standard_input():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) in nodes

def test_empty_nodes():
    nodes = []
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) is None

def test_single_node():
    nodes = ["node1"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key, vnodes_per_node=5) in nodes

def test_edge_case_key():
    nodes = ["node1", "node2", "node3"]
    key = ""
    assert get_consistent_hash_node(nodes, key) in nodes

def test_edge_case_nodes():
    nodes = ["node1"]
    key = ""
    assert get_consistent_hash_node(nodes, key) == "node1"