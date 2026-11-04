Here is a comprehensive suite of unit tests for the `check_half_open_overlap` function:

```python
# Test case 1: Intervals overlap partially
def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test case 2: Intervals do not overlap (adjacent)
def test_no_overlap_adjacent():
    assert check_half_open_overlap(1, 5, 5, 7) == False

# Test case 3: Intervals do not overlap (disjoint)
def test_no_overlap_disjoint():
    assert check_half_open_overlap(1, 5, 6, 7) == False

# Test case 4: One interval fully contains the other (should return False as per spec)
def test_fully_contained():
    assert check_half_open_overlap(1, 5, 2, 4) == False

# Test case 5: Intervals overlap at the start
def test_overlap_at_start():
    assert check_half_open_overlap(1, 5, 0, 3) == True

# Test case 6: Identical intervals (should return False as per spec)
def test_identical_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False
```

These test cases cover:
1. Partial overlap between intervals.
2. Non-overlapping adjacent intervals.
3. Non-overlapping disjoint intervals.
4. One interval fully containing another (which the function treats as non-overlapping per its specification).
5. Overlap at the start of one interval.
6. Identical intervals (also treated as non-overlapping per the function's logic).

The tests ensure the function behaves as expected for both standard and edge cases.