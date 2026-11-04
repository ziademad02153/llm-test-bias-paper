# Test standard input with overlapping intervals
def test_merge_overlapping_intervals_standard():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected_output = [(1, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with empty input
def test_merge_overlapping_intervals_empty():
    intervals = []
    expected_output = []
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with non-overlapping intervals
def test_merge_overlapping_intervals_non_overlapping():
    intervals = [(1, 2), (3, 4), (5, 6), (7, 8)]
    expected_output = [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with single interval
def test_merge_overlapping_intervals_single_interval():
    intervals = [(1, 10)]
    expected_output = [(1, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with overlapping intervals at bounds
def test_merge_overlapping_intervals_bounds():
    intervals = [(1, 5), (5, 10), (10, 15)]
    expected_output = [(1, 15)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with duplicate intervals
def test_merge_overlapping_intervals_duplicates():
    intervals = [(1, 5), (1, 5), (6, 10), (6, 10)]
    expected_output = [(1, 5), (6, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output