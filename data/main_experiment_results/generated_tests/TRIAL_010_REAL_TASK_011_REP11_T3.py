Here's a comprehensive suite of unit tests for the `check_half_open_overlap` function based on its specification:

```python
# Test case 1: Non-overlapping intervals (e1 <= s2)
def test_non_overlapping_intervals():
    assert not check_half_open_overlap(1, 3, 3, 5)

# Test case 2: Partially overlapping intervals (s1 < s2 < e1 < e2)
def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7)

# Test case 3: One interval completely within another (s1 < s2 < e2 < e1)
def test_interval_contained_within():
    assert check_half_open_overlap(1, 10, 3, 7)

# Test case 4: Adjacent but non-overlapping intervals (e1 == s2)
def test_adjacent_non_overlapping():
    assert not check_half_open_overlap(1, 2, 2, 3)

# Test case 5: Empty interval [s1, s1) should not overlap with any non-empty interval
def test_empty_first_interval():
    assert not check_half_open_overlap(2, 2, 1, 3)

# Test case 6: Both intervals are empty and at same point
def test_both_empty_intervals_same_point():
    assert not check_half_open_overlap(2, 2, 2, 2)