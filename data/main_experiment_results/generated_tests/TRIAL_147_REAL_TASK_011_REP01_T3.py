Here is a comprehensive suite of unit tests for the `check_half_open_overlap` function based on its specification:

```python
# Test case 1: Non-overlapping intervals (e1 <= s2)
def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 3, 5)

# Test case 2: Overlapping intervals (s1 < e2 and s2 < e1)
def test_overlapping_intervals():
    assert check_half_open_overlap(1, 5, 3, 7)

# Test case 3: One interval fully contained within another
def test_fully_contained_interval():
    assert check_half_open_overlap(2, 6, 3, 5)

# Test case 4: Adjacent intervals (e1 == s2) - should not overlap (half-open)
def test_adjacent_intervals_no_overlap():
    assert not check_half_open_overlap(1, 2, 2, 3)

# Test case 5: Empty interval (s1 == e1) - should not overlap with any non-empty interval
def test_empty_interval_no_overlap():
    assert not check_half_open_overlap(2, 2, 1, 3)

# Test case 6: Both intervals are empty (s1 == e1 and s2 == e2) - should not overlap
def test_both_empty_intervals_no_overlap():
    assert not check_half_open_overlap(1, 1, 2, 2)
```

These test cases cover:
1. Non-overlapping intervals
2. Overlapping intervals
3. One interval fully contained within another
4. Adjacent intervals (which should not overlap due to half-open nature)
5. Empty intervals (where start equals end)
6. Both intervals being empty

The tests follow the half-open interval semantics where `[s, e)` includes `s` but excludes `e`.