def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 5, 6, 10)

def test_partially_overlapping_intervals():
    assert check_half_open_overlap(1, 10, 5, 15)

def test_fully_overlapping_intervals():
    assert check_half_open_overlap(1, 10, 1, 10)

def test_edge_case_empty_interval():
    assert not check_half_open_overlap(1, 1, 2, 3)

def test_edge_case_equal_start_and_end():
    assert not check_half_open_overlap(1, 5, 5, 10)

def test_edge_case_negative_numbers():
    assert check_half_open_overlap(-5, 0, -3, 2)