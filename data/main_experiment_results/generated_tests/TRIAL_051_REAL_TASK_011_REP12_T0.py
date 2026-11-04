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
def test_contained_interval(): 
    assert check_half_open_overlap(1, 7, 2, 6) == True

# Test invalid input (non-integer values)
def test_invalid_input():
    try:
        check_half_open_overlap(1.5, 5, 3, 7)
        assert False, "Expected TypeError for non-integer input"
    except TypeError:
        pass

# Test invalid input (start value greater than end value)
def test_invalid_range():
    try:
        check_half_open_overlap(5, 1, 3, 7)
        assert False, "Expected ValueError for invalid range"
    except ValueError:
        pass