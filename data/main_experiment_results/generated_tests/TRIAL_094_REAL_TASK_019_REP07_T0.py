# Test standard input with overlapping intervals
def test_merge_overlapping_intervals():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected_output = [(1, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test standard input with non-overlapping intervals
def test_merge_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (8, 10), (15, 18)]
    expected_output = [(1, 3), (4, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with empty input
def test_merge_empty_intervals():
    intervals = []
    expected_output = []
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with single interval
def test_merge_single_interval():
    intervals = [(1, 3)]
    expected_output = [(1, 3)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with duplicate intervals
def test_merge_duplicate_intervals():
    intervals = [(1, 3), (1, 3)]
    expected_output = [(1, 3)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with unsorted intervals
def test_merge_unsorted_intervals():
    intervals = [(8, 10), (1, 3), (2, 6), (15, 18)]
    expected_output = [(1, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output