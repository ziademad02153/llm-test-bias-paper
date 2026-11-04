# Test standard overlapping intervals
def test_overlap(): 
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test non-overlapping intervals
def test_no_overlap(): 
    assert check_half_open_overlap(1, 3, 4, 7) == False

# Test edge case where intervals touch but do not overlap
def test_touch_no_overlap(): 
    assert check_half_open_overlap(1, 3, 3, 7) == False

# Test edge case where one interval is empty
def test_empty_interval(): 
    assert check_half_open_overlap(1, 1, 2, 3) == False

# Test edge case where both intervals are empty
def test_both_empty_intervals(): 
    assert check_half_open_overlap(1, 1, 2, 2) == False

# Test edge case where intervals are equal
def test_equal_intervals(): 
    assert check_half_open_overlap(1, 3, 1, 3) == False