def test_merge_overlapping_intervals_standard_input():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected_output = [(1, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_empty_input():
    intervals = []
    expected_output = []
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_single_interval():
    intervals = [(1, 3)]
    expected_output = [(1, 3)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_adjacent_intervals():
    intervals = [(1, 3), (3, 5), (6, 8), (8, 10)]
    expected_output = [(1, 3), (3, 5), (6, 8), (8, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_overlapping_intervals():
    intervals = [(1, 5), (2, 4), (6, 8), (7, 9)]
    expected_output = [(1, 5), (6, 9)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_unsorted_intervals():
    intervals = [(5, 7), (1, 3), (2, 4), (6, 8)]
    expected_output = [(1, 4), (5, 7), (6, 8)]
    assert merge_overlapping_intervals(intervals) == expected_output