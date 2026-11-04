def test_no_overlap():
    assert not check_half_open_overlap(1, 3, 4, 6)

def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7)

def test_adjacent_intervals_no_overlap():
    assert not check_half_open_overlap(1, 3, 3, 5)

def test_one_interval_inside_another():
    assert check_half_open_overlap(2, 8, 3, 5)

def test_empty_interval_no_overlap():
    assert not check_half_open_overlap(1, 1, 2, 3)

def test_both_empty_intervals_no_overlap():
    assert not check_half_open_overlap(1, 1, 2, 2)