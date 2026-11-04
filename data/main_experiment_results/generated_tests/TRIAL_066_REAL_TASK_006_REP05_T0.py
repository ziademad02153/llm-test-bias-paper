import hashlib

def test_get_consistent_hash_node_standard_input():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) in nodes

def test_get_consistent_hash_node_empty_nodes():
    nodes = []
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) is None

def test_get_consistent_hash_node_empty_key():
    nodes = ["node1", "node2", "node3"]
    key = ""
    assert get_consistent_hash_node(nodes, key) in nodes

def test_get_consistent_hash_node_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key, vnodes_per_node=5) in nodes

def test_get_consistent_hash_node_hash_collision():
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    assert get_consistent_hash_node(nodes, key1) == get_consistent_hash_node(nodes, key2) or get_consistent_hash_node(nodes, key1)!= get_consistent_hash_node(nodes, key2)

def test_get_consistent_hash_node_md5_hash():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    md5_hash = int(hashlib.md5(key.encode()).hexdigest(), 16)
    assert get_consistent_hash_node(nodes, key) in nodes