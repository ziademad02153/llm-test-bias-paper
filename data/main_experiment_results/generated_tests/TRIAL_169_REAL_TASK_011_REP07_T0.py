# Test standard overlapping intervals
def test_overlap(): 
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test non-overlapping intervals
def test_no_overlap(): 
    assert check_half_open_overlap(1, 3, 4, 7) == False

# Test edge case where intervals touch but do not overlap
def test_touch_no_overlap(): 
    assert check_half_open_overlap(1, 3, 3, 7) == False

# Test edge case where one interval is contained within the other
def test_contained_no_overlap(): 
    assert check_half_open_overlap(1, 7, 2, 6) == False

# Test edge case with negative numbers
def test_negative_overlap(): 
    assert check_half_open_overlap(-3, 1, -2, 2) == True

# Test edge case with zero
def test_zero_overlap(): 
    assert check_half_open_overlap(0, 5, 3, 7) == True