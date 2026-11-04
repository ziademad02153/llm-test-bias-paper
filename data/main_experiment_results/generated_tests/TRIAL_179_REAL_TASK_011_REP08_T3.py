# Test standard overlapping intervals
assert check_half_open_overlap(1, 5, 3, 7) == True

# Test non-overlapping intervals
assert check_half_open_overlap(1, 3, 4, 6) == False

# Test intervals that share a boundary but do not overlap
assert check_half_open_overlap(1, 5, 5, 8) == False

# Test intervals where one is completely within the other
assert check_half_open_overlap(2, 6, 3, 5) == True

# Test intervals with negative values
assert check_half_open_overlap(-5, 0, -3, 2) == True

# Test intervals where one interval is empty
assert check_half_open_overlap(1, 1, 2, 4) == False