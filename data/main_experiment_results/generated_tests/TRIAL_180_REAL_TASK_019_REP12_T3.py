def test_empty_list():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (7, 9)]

def test_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 8)]

def test_contiguous_intervals():
    intervals = [(1, 3), (3, 5), (5, 7)]
    assert merge_overlapping_intervals(intervals) == [(1, 7)]

def test_single_interval():
    intervals = [(1, 5)]
    assert merge_overlapping_intervals(intervals) == [(1, 5)]

def test_complex_overlapping():
    intervals = [(1, 10), (2, 5), (6, 8), (8, 10), (15, 20)]
    assert merge_overlapping_intervals(intervals) == [(1, 10), (15, 20)]