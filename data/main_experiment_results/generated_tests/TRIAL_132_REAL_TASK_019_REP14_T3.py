def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (8, 10)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (8, 10)]

def test_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (7, 9)]

def test_adjacent_intervals():
    intervals = [(1, 3), (3, 6), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 8)]

def test_single_interval():
    intervals = [(5, 10)]
    assert merge_overlapping_intervals(intervals) == [(5, 10)]

def test_complex_overlap():
    intervals = [(1, 5), (2, 6), (3, 8), (10, 15), (12, 18), (20, 22)]
    assert merge_overlapping_intervals(intervals) == [(1, 8), (10, 18), (20, 22)]