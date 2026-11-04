import hashlib
import bisect

def get_consistent_hash_node(nodes: list[str], key: str, vnodes_per_node: int = 3) -> str | None:
    # Check if the list of nodes is empty
    if not nodes:
        return None

    # Create a list to store the virtual nodes
    vnodes = []

    # Create a list to store the hashes of the virtual nodes
    vnode_hashes = []

    # For each physical node
    for node in nodes:
        # For each virtual node
        for i in range(vnodes_per_node):
            # Create a virtual node name
            vnode = f"{node}-{i}"

            # Hash the virtual node name using MD5
            vnode_hash = int(hashlib.md5(vnode.encode()).hexdigest(), 16)

            # Add the virtual node and its hash to the lists
            vnodes.append(vnode)
            vnode_hashes.append(vnode_hash)

    # Sort the lists of virtual nodes and their hashes
    sorted_vnode_hashes, sorted_vnodes = zip(*sorted(zip(vnode_hashes, vnodes)))

    # Hash the key using MD5
    key_hash = int(hashlib.md5(key.encode()).hexdigest(), 16)

    # Find the index where the key hash should be inserted in the sorted list of virtual node hashes
    index = bisect.bisect(sorted_vnode_hashes, key_hash)

    # If the index is equal to the length of the list, it means the key hash is greater than all virtual node hashes
    # In this case, we wrap around to the start of the list
    if index == len(sorted_vnode_hashes):
        index = 0

    # Return the physical node name of the virtual node where the key is distributed
    return sorted_vnodes[index].split('-')[0]

def test_empty_nodes():
    assert get_consistent_hash_node([], "key") is None

def test_single_node():
    assert get_consistent_hash_node(["node1"], "key") == "node1"

def test_multiple_nodes():
    nodes = ["node1", "node2", "node3"]
    key = "key"
    result = get_consistent_hash_node(nodes, key)
    assert result in nodes

def test_vnodes_per_node():
    nodes = ["node1", "node2", "node3"]
    key = "key"
    result1 = get_consistent_hash_node(nodes, key, vnodes_per_node=3)
    result2 = get_consistent_hash_node(nodes, key, vnodes_per_node=5)
    assert result1 in nodes
    assert result2 in nodes

def test_same_key_different_nodes():
    nodes1 = ["node1", "node2", "node3"]
    nodes2 = ["node4", "node5", "node6"]
    key = "key"
    result1 = get_consistent_hash_node(nodes1, key)
    result2 = get_consistent_hash_node(nodes2, key)
    assert result1 in nodes1
    assert result2 in nodes2
    assert result1!= result2

def test_different_keys_same_nodes():
    nodes = ["node1", "node2", "node3"]
    key1 = "key1"
    key2 = "key2"
    result1 = get_consistent_hash_node(nodes, key1)
    result2 = get_consistent_hash_node(nodes, key2)
    assert result1 in nodes
    assert result2 in nodes
    assert result1!= result2

test_empty_nodes()
test_single_node()
test_multiple_nodes()
test_vnodes_per_node()
test_same_key_different_nodes()
test_different_keys_same_nodes()