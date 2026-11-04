def test_no_overlap():
    assert not check_half_open_overlap(1, 3, 4, 6)

def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7)

def test_adjacent_no_overlap():
    assert not check_half_open_overlap(1, 3, 3, 5)

def test_one_interval_inside_other():
    assert check_half_open_overlap(2, 8, 3, 5)

def test_empty_interval_first():
    assert not check_half_open_overlap(3, 3, 1, 5)

def test_empty_interval_second():
    assert not check_half_open_overlap(1, 5, 6, 6)