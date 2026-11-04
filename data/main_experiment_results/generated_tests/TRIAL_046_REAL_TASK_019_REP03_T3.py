Here's a comprehensive suite of unit tests for the `merge_overlapping_intervals` function based on its specification:

```python
# Test case 1: No overlapping intervals
def test_no_overlaps():
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (7, 9)]

# Test case 2: Adjacent intervals (should merge)
def test_adjacent_intervals():
    intervals = [(1, 3), (3, 5), (5, 7)]
    assert merge_overlapping_intervals(intervals) == [(1, 7)]

# Test case 3: Overlapping intervals (should merge)
def test_overlapping_intervals():
    intervals = [(1, 4), (2, 5), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 8)]

# Test case 4: Empty input
def test_empty_input():
    assert merge_overlapping_intervals([]) == []

# Test case 5: Single interval
def test_single_interval():
    assert merge_overlapping_intervals([(1, 5)]) == [(1, 5)]

# Test case 6: Multiple overlapping intervals merging into one
def test_multiple_overlaps_merge_to_one():
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6)]
    assert merge_overlapping_intervals(intervals) == [(1, 6)]