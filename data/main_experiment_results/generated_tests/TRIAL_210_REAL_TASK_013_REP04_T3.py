# Test standard inputs: overlapping intervals
assert intersect_intervals(1, 5, 3, 7) == (3, 5)

# Test standard inputs: non-overlapping intervals
assert intersect_intervals(1, 3, 4, 6) is None

# Test edge case: one interval is unbounded on the left
assert intersect_intervals(None, 5, 3, 7) == (3, 5)

# Test edge case: one interval is unbounded on the right
assert intersect_intervals(1, None, 3, 7) == (3, 7)

# Test edge case: both intervals are unbounded
assert intersect_intervals(None, None, None, None) == (None, None)

# Test edge case: one interval is empty (start > end)
assert intersect_intervals(5, 3, 1, 7) is None