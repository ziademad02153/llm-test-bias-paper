Here is a suite of comprehensive unit tests for the `check_half_open_overlap` function based on its specification:

```python
# Test case 1: Non-overlapping intervals
def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 4, 6)

# Test case 2: Partially overlapping intervals
def test_partially_overlapping_intervals():
    assert check_half_open_overlap(1, 5, 3, 7)

# Test case 3: Adjacent but non-overlapping intervals
def test_adjacent_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 3, 5)

# Test case 4: One interval completely inside the other
def test_one_interval_inside_other():
    assert check_half_open_overlap(2, 8, 4, 6)

# Test case 5: Identical intervals
def test_identical_intervals():
    assert check_half_open_overlap(3, 7, 3, 7)

# Test case 6: Empty intervals (edge case)
def test_empty_intervals():
    assert not check_half_open_overlap(2, 2, 3, 3)
```

This test suite covers:
1. Non-overlapping intervals
2. Partially overlapping intervals
3. Adjacent intervals (which should not overlap in half-open notation)
4. One interval fully contained within another
5. Identical intervals (should overlap)
6. Empty intervals (edge case where start equals end)

All test cases are based strictly on the function's specification and the behavior of half-open intervals [s, e). The tests are independent and can be run in any order.