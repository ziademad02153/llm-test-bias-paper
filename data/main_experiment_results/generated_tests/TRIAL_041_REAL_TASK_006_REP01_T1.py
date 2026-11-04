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
    assert get_consistent_hash_node(nodes, key) == nodes[0]

def test_get_consistent_hash_node_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    vnodes_per_node = 5
    assert get_consistent_hash_node(nodes, key, vnodes_per_node) in nodes

def test_get_consistent_hash_node_key_hash_collision():
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    assert get_consistent_hash_node(nodes, key1) is not None
    assert get_consistent_hash_node(nodes, key2) is not None

def test_get_consistent_hash_node_large_input():
    nodes = [f"node{i}" for i in range(100)]
    key = "test_key"
    assert get_consistent_hash_node(nodes, key) in nodes

# Test that the function is deterministic
def test_get_consistent_hash_node_determinism():
    nodes = ["node1", "node2", "node3"]
    key = "test_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2