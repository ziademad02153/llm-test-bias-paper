def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert merge_overlapping_intervals(intervals) == [(1, 2), (3, 4), (5, 6)]

def test_overlapping_intervals():
    intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 4), (5, 8)]

def test_adjacent_intervals():
    intervals = [(1, 2), (2, 3), (3, 4)]
    assert merge_overlapping_intervals(intervals) == [(1, 4)]

def test_single_interval():
    intervals = [(1, 5)]
    assert merge_overlapping_intervals(intervals) == [(1, 5)]

def test_unsorted_intervals():
    intervals = [(5, 6), (1, 3), (2, 4)]
    assert merge_overlapping_intervals(intervals) == [(1, 4), (5, 6)]