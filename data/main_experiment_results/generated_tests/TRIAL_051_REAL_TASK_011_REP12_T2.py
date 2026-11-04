def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 4, 6)

def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7)

def test_adjacent_intervals_no_overlap():
    assert not check_half_open_overlap(1, 5, 5, 7)

def test_one_interval_fully_contained_no_overlap():
    assert not check_half_open_overlap(2, 6, 3, 5)

def test_overlap_at_start():
    assert check_half_open_overlap(1, 5, 0, 3)

def test_overlap_at_end():
    assert check_half_open_overlap(1, 5, 4, 6)