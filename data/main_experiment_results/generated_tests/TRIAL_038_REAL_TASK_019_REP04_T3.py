def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 3)]) == [(1, 3)]

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (7, 9)]

def test_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 8)]

def test_contiguous_intervals():
    intervals = [(1, 3), (3, 5), (5, 7)]
    assert merge_overlapping_intervals(intervals) == [(1, 7)]

def test_complex_overlapping_intervals():
    intervals = [(1, 5), (2, 4), (6, 8), (7, 9), (10, 12)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 9), (10, 12)]