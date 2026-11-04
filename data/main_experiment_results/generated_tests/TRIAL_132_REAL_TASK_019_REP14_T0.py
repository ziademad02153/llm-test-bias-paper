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
    intervals = [(1, 3), (3, 5)]
    expected_output = [(1, 5)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_non_overlapping_intervals():
    intervals = [(1, 3), (5, 7), (9, 11)]
    expected_output = [(1, 3), (5, 7), (9, 11)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_merge_overlapping_intervals_overlapping_intervals_with_same_start():
    intervals = [(1, 3), (1, 5), (6, 8)]
    expected_output = [(1, 5), (6, 8)]
    assert merge_overlapping_intervals(intervals) == expected_output