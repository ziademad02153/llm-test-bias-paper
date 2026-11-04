# Test cases for check_half_open_overlap function

# Test 1: Intervals overlap partially
def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test 2: Intervals do not overlap (end of first interval equals start of second)
def test_no_overlap_edge():
    assert check_half_open_overlap(1, 5, 5, 7) == False

# Test 3: Intervals overlap partially (second interval starts before first ends)
def test_partial_overlap_reverse():
    assert check_half_open_overlap(1, 5, 0, 3) == True

# Test 4: Intervals do not overlap (first interval ends before second starts)
def test_no_overlap():
    assert check_half_open_overlap(1, 5, 6, 7) == False

# Test 5: One interval fully contained within the other
def test_fully_contained():
    assert check_half_open_overlap(2, 6, 3, 5) == False

# Test 6: Intervals are identical
def test_identical_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == True