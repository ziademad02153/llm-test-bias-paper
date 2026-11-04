def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 3)]) == [(1, 3)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (4, 6)]) == [(1, 3), (4, 6)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 4), (2, 5)]) == [(1, 5)]

def test_adjacent_intervals():
    assert merge_overlapping_intervals([(1, 3), (3, 6)]) == [(1, 6)]

def test_multiple_overlaps():
    assert merge_overlapping_intervals([(1, 3), (2, 6), (5, 8)]) == [(1, 8)]