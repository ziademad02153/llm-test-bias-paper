def test_overlapping_intervals():
    assert check_half_open_overlap(1, 5, 3, 7) == True

def test_non_overlapping_intervals():
    assert check_half_open_overlap(1, 3, 5, 7) == False

def test_adjacent_intervals_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 9) == False

def test_one_interval_inside_another():
    assert check_half_open_overlap(2, 8, 3, 6) == True

def test_negative_intervals_overlap():
    assert check_half_open_overlap(-5, 0, -3, 3) == True

def test_empty_interval():
    assert check_half_open_overlap(1, 1, 2, 4) == False