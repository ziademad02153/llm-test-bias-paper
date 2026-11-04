def test_partial_overlap():
    # Partial overlap where intervals share some common range
    assert check_half_open_overlap(1, 5, 3, 7) == True

def test_no_overlap():
    # No overlap with intervals adjacent but not overlapping
    assert check_half_open_overlap(1, 5, 5, 7) == False

def test_contained_overlap():
    # One interval fully contained within another (should return False as per spec)
    assert check_half_open_overlap(2, 6, 3, 5) == False

def test_non_overlapping_intervals():
    # Non-overlapping intervals with a gap
    assert check_half_open_overlap(1, 3, 4, 6) == False

def test_reverse_order_overlap():
    # Intervals specified in reverse order but still overlapping
    assert check_half_open_overlap(5, 10, 1, 6) == True

def test_single_point_non_overlap():
    # Single-point intervals that do not overlap
    assert check_half_open_overlap(1, 2, 2, 3) == False