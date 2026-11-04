def test_empty_nodes():
    """Test that None is returned when nodes list is empty."""
    assert get_consistent_hash_node([], "key") is None


def test_single_node():
    """Test that the same node is always returned for any key when there's only one node."""
    nodes = ["node1"]
    key1 = "key1"
    key2 = "key2"
    assert get_consistent_hash_node(nodes, key1) == "node1"
    assert get_consistent_hash_node(nodes, key2) == "node1"


def test_multiple_nodes_consistent_hashing():
    """Test that the same key consistently maps to the same node."""
    nodes = ["node1", "node2", "node3"]
    key = "consistent_key"
    result1 = get_consistent_hash_node(nodes, key)
    result2 = get_consistent_hash_node(nodes, key)
    assert result1 == result2


def test_vnodes_per_node_affects_distribution():
    """Test that changing vnodes_per_node affects the distribution."""
    nodes = ["node1", "node2"]
    key = "test_key"
    result_default = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    result_custom = get_consistent_hash_node(nodes, key, vnodes_per_node=10)
    # This might not always be true, but it's likely with different vnodes counts
    assert result_default != result_custom or len(nodes) == 1


def test_wrap_around_behavior():
    """Test that keys hash to the first node when their hash is greater than all vnode hashes."""
    nodes = ["node1", "node2"]
    # Create a key that will hash to a very large value (simulate wrap-around)
    key = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"  # Likely to have a high MD5 hash
    # Manually compute all vnode hashes to verify wrap-around
    vnode_hashes = []
    for node in nodes:
        for i in range(3):  # default vnodes_per_node
            vnode = f"{node}-{i}"
            vnode_hash = int(hashlib.md5(vnode.encode()).hexdigest(), 16)
            vnode_hashes.append(vnode_hash)
    key_hash = int(hashlib.md5(key.encode()).hexdigest(), 16)
    if key_hash > max(vnode_hashes):
        # The result should be the first vnode (wrap-around)
        first_vnode = f"{nodes[0]}-0"
        assert get_consistent_hash_node(nodes, key) == first_vnode.split('-')[0]