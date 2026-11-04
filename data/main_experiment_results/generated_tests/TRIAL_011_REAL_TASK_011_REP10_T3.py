# Test case 1: Overlapping intervals
assert check_half_open_overlap(1, 5, 3, 7) == True

# Test case 2: Non-overlapping intervals
assert check_half_open_overlap(1, 3, 4, 6) == False

# Test case 3: Adjacent intervals (no overlap)
assert check_half_open_overlap(1, 4, 4, 6) == False

# Test case 4: One interval completely inside the other
assert check_half_open_overlap(2, 8, 3, 5) == True

# Test case 5: Empty interval (s1 == e1)
assert check_half_open_overlap(3, 3, 1, 5) == False

# Test case 6: Both intervals empty (no overlap)
assert check_half_open_overlap(2, 2, 4, 4) == False