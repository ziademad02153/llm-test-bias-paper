Here's a comprehensive suite of unit tests for the `merge_overlapping_intervals` function:

```python
def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (4, 6), (8, 10)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (4, 6), (8, 10)]

def test_adjacent_intervals():
    intervals = [(1, 4), (4, 6), (6, 8)]
    assert merge_overlapping_intervals(intervals) == [(1, 8)]

def test_fully_overlapping_intervals():
    intervals = [(1, 10), (2, 5), (3, 7)]
    assert merge_overlapping_intervals(intervals) == [(1, 10)]

def test_mixed_overlapping_and_non_overlapping():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    assert merge_overlapping_intervals(intervals) == [(1, 6), (8, 10), (15, 18)]

def test_unsorted_intervals():
    intervals = [(5, 8), (1, 3), (6, 9), (2, 4)]
    assert merge_overlapping_intervals(intervals) == [(1, 4), (5, 9)]