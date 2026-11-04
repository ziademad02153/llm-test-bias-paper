def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (7, 9)]

def test_overlapping_intervals():
    intervals = [(1, 5), (3, 7), (8, 10)]
    assert merge_overlapping_intervals(intervals) == [(1, 7), (8, 10)]

def test_adjacent_intervals():
    intervals = [(1, 3), (3, 5), (5, 7)]
    assert merge_overlapping_intervals(intervals) == [(1, 7)]

def test_single_interval():
    intervals = [(1, 2)]
    assert merge_overlapping_intervals(intervals) == [(1, 2)]

def test_complex_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (6, 8), (7, 9), (10, 12)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 9), (10, 12)]