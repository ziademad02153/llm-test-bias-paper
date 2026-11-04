def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 5)]) == [(1, 5)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (4, 6), (7, 9)]) == [(1, 3), (4, 6), (7, 9)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 5), (3, 7), (8, 10)]) == [(1, 7), (8, 10)]

def test_adjacent_intervals():
    assert merge_overlapping_intervals([(1, 4), (4, 6), (6, 9)]) == [(1, 9)]

def test_complex_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 6), (5, 7), (8, 10), (9, 12)]) == [(1, 7), (8, 12)]