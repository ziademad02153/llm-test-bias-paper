# Test standard overlapping intervals
def test_standard_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test non-overlapping intervals
def test_no_overlap():
    assert check_half_open_overlap(1, 3, 4, 7) == False

# Test edge case: identical intervals
def test_identical_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False

# Test edge case: one interval is a subset of the other
def test_subset_interval():
    assert check_half_open_overlap(1, 5, 2, 4) == True

# Test edge case: intervals share a boundary
def test_shared_boundary():
    assert check_half_open_overlap(1, 3, 3, 5) == False

# Test edge case: intervals have zero length
def test_zero_length_interval():
    assert check_half_open_overlap(1, 1, 2, 3) == False