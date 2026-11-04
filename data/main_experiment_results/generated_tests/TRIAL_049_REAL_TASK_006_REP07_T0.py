import hashlib
import bisect

def test_get_consistent_hash_node_standard_input():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) in nodes

def test_get_consistent_hash_node_empty_nodes():
    nodes = []
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) is None

def test_get_consistent_hash_node_empty_key():
    nodes = ["node1", "node2", "node3"]
    key = ""
    assert get_consistent_hash_node(nodes, key) in nodes

def test_get_consistent_hash_node_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key, vnodes_per_node=5) in nodes

def test_get_consistent_hash_node_single_node():
    nodes = ["node1"]
    key = "example_key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_get_consistent_hash_node_multiple_keys():
    nodes = ["node1", "node2", "node3"]
    key1 = "example_key1"
    key2 = "example_key2"
    assert get_consistent_hash_node(nodes, key1) in nodes
    assert get_consistent_hash_node(nodes, key2) in nodes