# Test case 1: Standard overlapping intervals
assert intersect_intervals(1, 5, 3, 7) == (3, 5)

# Test case 2: Non-overlapping intervals
assert intersect_intervals(1, 3, 4, 6) is None

# Test case 3: One interval is unbounded on the left
assert intersect_intervals(None, 5, 2, 7) == (2, 5)

# Test case 4: One interval is unbounded on the right
assert intersect_intervals(3, None, 1, 5) == (3, 5)

# Test case 5: Both intervals are unbounded
assert intersect_intervals(None, None, None, None) == (None, None)

# Test case 6: One interval is entirely within the other
assert intersect_intervals(2, 6, 3, 5) == (3, 5)