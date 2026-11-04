# Test case 1: Intervals overlap partially
def test_overlap_partial():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test case 2: Intervals do not overlap (end of first interval equals start of second interval)
def test_no_overlap_edge():
    assert check_half_open_overlap(1, 5, 5, 7) == False

# Test case 3: Intervals overlap partially (start of first interval equals end of second interval)
def test_overlap_edge():
    assert check_half_open_overlap(1, 5, 0, 3) == True

# Test case 4: Intervals do not overlap (first interval is entirely before the second)
def test_no_overlap_before():
    assert check_half_open_overlap(1, 5, 6, 7) == False

# Test case 5: Intervals do not overlap (first interval is entirely after the second)
def test_no_overlap_after():
    assert check_half_open_overlap(6, 7, 1, 5) == False

# Test case 6: One interval is fully contained within the other
def test_no_overlap_contained():
    assert check_half_open_overlap(2, 4, 1, 5) == False