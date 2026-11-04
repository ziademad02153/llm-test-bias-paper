import hashlib
import bisect

# Assuming the function under test is already imported as get_consistent_hash_node

def test_empty_nodes():
    assert get_consistent_hash_node([], "key") is None

def test_single_node():
    nodes = ["node1"]
    key = "key"
    assert get_consistent_hash_node(nodes, key) == "node1"

def test_multiple_nodes():
    nodes = ["node1", "node2", "node3"]
    key = "key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "key"
    vnodes_per_node = 5
    result = get_consistent_hash_node(nodes, key, vnodes_per_node)
    assert result in nodes

def test_key_distribution():
    nodes = ["node1", "node2", "node3"]
    keys = ["key1", "key2", "key3"]
    results = [get_consistent_hash_node(nodes, key) for key in keys]
    assert len(set(results)) > 1

def test_hash_collision():
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = hashlib.md5(key1.encode()).hexdigest()
    assert get_consistent_hash_node(nodes, key1) == get_consistent_hash_node(nodes, key2)

test_empty_nodes()
test_single_node()
test_multiple_nodes()
test_vnodes_per_node()
test_key_distribution()
test_hash_collision()