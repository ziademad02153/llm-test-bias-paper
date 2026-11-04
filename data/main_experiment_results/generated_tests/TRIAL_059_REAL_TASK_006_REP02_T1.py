import hashlib
import bisect

def test_get_consistent_hash_node_standard_input():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) in nodes

def test_get_consistent_hash_node_empty_nodes():
    nodes = []
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) is None

def test_get_consistent_hash_node_single_node():
    nodes = ["node1"]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_get_consistent_hash_node_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    vnodes_per_node = 5
    assert get_consistent_hash_node(nodes, key, vnodes_per_node) in nodes

def test_get_consistent_hash_node_same_key_different_nodes():
    nodes1 = ["node1", "node2", "node3"]
    nodes2 = ["node4", "node5", "node6"]
    key = "test_key"
    assert get_consistent_hash_node(nodes1, key)!= get_consistent_hash_node(nodes2, key)

def test_get_consistent_hash_node_same_key_same_nodes():
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    assert get_consistent_hash_node(nodes, key1) in nodes
    assert get_consistent_hash_node(nodes, key2) in nodes