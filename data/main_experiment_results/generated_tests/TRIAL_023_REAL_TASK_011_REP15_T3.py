def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 4, 6)

def test_overlapping_intervals():
    assert check_half_open_overlap(1, 5, 3, 7)

def test_adjacent_intervals_no_overlap():
    assert not check_half_open_overlap(1, 3, 3, 5)

def test_one_interval_inside_another():
    assert check_half_open_overlap(2, 8, 3, 5)

def test_same_intervals():
    assert check_half_open_overlap(1, 4, 1, 4)

def test_empty_intervals():
    assert not check_half_open_overlap(2, 2, 3, 3)