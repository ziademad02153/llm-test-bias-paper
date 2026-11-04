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

# Test edge case with single interval
def test_merge_overlapping_intervals_single():
    intervals = [(1, 3)]
    expected_output = [(1, 3)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with non-overlapping intervals
def test_merge_overlapping_intervals_non_overlapping():
    intervals = [(1, 3), (4, 6), (7, 9)]
    expected_output = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with fully overlapping intervals
def test_merge_overlapping_intervals_fully_overlapping():
    intervals = [(1, 10), (2, 5), (3, 7)]
    expected_output = [(1, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

# Test edge case with unsorted input
def test_merge_overlapping_intervals_unsorted():
    intervals = [(5, 7), (1, 3), (2, 6), (8, 10)]
    expected_output = [(1, 7), (8, 10)]
    assert merge_overlapping_intervals(intervals) == expected_output

test_merge_overlapping_intervals_standard()
test_merge_overlapping_intervals_empty()
test_merge_overlapping_intervals_single()
test_merge_overlapping_intervals_non_overlapping()
test_merge_overlapping_intervals_fully_overlapping()
test_merge_overlapping_intervals_unsorted()