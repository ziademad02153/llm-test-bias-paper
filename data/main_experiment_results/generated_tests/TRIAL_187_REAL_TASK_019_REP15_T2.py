def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (7, 9)]

def test_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (7, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (7, 8)]

def test_adjacent_intervals():
    intervals = [(1, 3), (3, 6), (6, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 9)]

def test_single_interval():
    intervals = [(1, 5)]
    assert merge_overlapping_intervals(intervals) == [(1, 5)]

def test_unsorted_intervals():
    intervals = [(5, 8), (1, 3), (4, 6)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 8)]