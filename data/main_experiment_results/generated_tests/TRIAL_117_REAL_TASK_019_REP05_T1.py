# Test standard input with overlapping intervals
def test_merge_overlapping_intervals():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected_output = [(1, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test standard input with non-overlapping intervals
def test_merge_non_overlapping_intervals():
    intervals = [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)]
    expected_output = [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with empty input
def test_empty_input():
    intervals = []
    expected_output = []
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with single interval
def test_single_interval():
    intervals = [(1, 10)]
    expected_output = [(1, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with duplicate intervals
def test_duplicate_intervals():
    intervals = [(1, 10), (1, 10), (1, 10)]
    expected_output = [(1, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with unsorted intervals
def test_unsorted_intervals():
    intervals = [(5, 10), (1, 3), (2, 6), (8, 10), (15, 18)]
    expected_output = [(1, 6), (5, 10), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == [(1, 6), (5, 10), (8, 10), (15, 18)]