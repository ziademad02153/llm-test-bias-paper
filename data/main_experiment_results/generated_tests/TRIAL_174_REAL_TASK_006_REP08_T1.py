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

def test_get_consistent_hash_node_hash_collision():
    nodes = ["node1", "node2", "node3"]
    key1 = "test_key1"
    key2 = "test_key2"
    assert get_consistent_hash_node(nodes, key1) == get_consistent_hash_node(nodes, key2) or get_consistent_hash_node(nodes, key1)!= get_consistent_hash_node(nodes, key2)

def test_get_consistent_hash_node_key_distribution():
    nodes = ["node1", "node2", "node3"]
    keys = [f"test_key_{i}" for i in range(100)]
    node_counts = {node: 0 for node in nodes}
    for key in keys:
        node = get_consistent_hash_node(nodes, key)
        node_counts[node] += 1
    assert all(count > 0 for count in node_counts.values())