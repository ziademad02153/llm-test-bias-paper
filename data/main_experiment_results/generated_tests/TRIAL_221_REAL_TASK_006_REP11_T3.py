# Test 1: Standard case with multiple nodes and a key
def test_standard_case():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes, "The result should be one of the provided nodes."

# Test 2: Edge case with empty nodes list
def test_empty_nodes():
    nodes = []
    key = "example_key"
    result = get_consistent_hash_node(nodes, key)
    assert result is None, "The result should be None when nodes list is empty."

# Test 3: Edge case with empty key
def test_empty_key():
    nodes = ["node1", "node2", "node3"]
    key = ""
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes, "The result should be one of the provided nodes even with an empty key."

# Test 4: Edge case with single node
def test_single_node():
    nodes = ["node1"]
    key = "example_key"
    result = get_consistent_hash_node(nodes, key)
    assert result == "node1", "The result should be the single node provided."

# Test 5: Test with custom virtual nodes per node
def test_custom_vnodes():
    nodes = ["node1", "node2", "node3"]
    key = "example_key"
    vnodes_per_node = 5
    result = get_consistent_hash_node(nodes, key, vnodes_per_node)
    assert result in nodes, "The result should be one of the provided nodes with custom vnodes_per_node."

# Test 6: Test with None key
def test_none_key():
    nodes = ["node1", "node2", "node3"]
    key = None
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes, "The result should be one of the provided nodes even with a None key."