def test_no_overlap():
    # Intervals do not overlap
    assert not check_half_open_overlap(1, 3, 4, 6)

def test_partial_overlap():
    # Intervals partially overlap
    assert check_half_open_overlap(1, 5, 3, 7)

def test_adjacent_no_overlap():
    # Adjacent intervals (e1 == s2) do not overlap (half-open)
    assert not check_half_open_overlap(1, 3, 3, 5)

def test_one_interval_inside_another():
    # One interval is entirely inside the other
    assert check_half_open_overlap(2, 8, 3, 5)

def test_empty_interval_first():
    # First interval is empty (s1 == e1)
    assert not check_half_open_overlap(3, 3, 2, 5)

def test_empty_interval_second():
    # Second interval is empty (s2 == e2)
    assert not check_half_open_overlap(1, 4, 5, 5)