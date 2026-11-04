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
    assert check_half_open_overlap(1, 7, 3, 5) == True

# Test edge case where intervals have the same start and end points
def test_same_interval(): 
    assert check_half_open_overlap(1, 5, 1, 5) == False

# Test edge case where interval end points are equal
def test_equal_end_points(): 
    assert check_half_open_overlap(1, 5, 1, 5) == False