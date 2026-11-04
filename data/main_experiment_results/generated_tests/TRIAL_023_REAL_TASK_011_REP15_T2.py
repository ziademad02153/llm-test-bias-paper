Here is a comprehensive suite of unit tests for the `check_half_open_overlap` function, covering standard cases, edge cases, and bounds:

```python
# Test case 1: Intervals overlap partially (s1 < s2 < e1 < e2)
def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test case 2: Intervals are adjacent (e1 == s2)
def test_adjacent_intervals_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 7) == False

# Test case 3: Intervals do not overlap (e1 < s2)
def test_no_overlap():
    assert check_half_open_overlap(1, 5, 6, 7) == False

# Test case 4: One interval fully contains the other (should return False as per spec)
def test_fully_contained_no_overlap():
    assert check_half_open_overlap(1, 7, 3, 5) == False

# Test case 5: Intervals are identical (should return False as per spec)
def test_identical_intervals_no_overlap():
    assert check_half_open_overlap(1, 5, 1, 5) == False

# Test case 6: Intervals overlap at the start (s2 < s1 < e2 < e1)
def test_overlap_at_start():
    assert check_half_open_overlap(3, 7, 1, 4) == True
```

### Explanation of Test Cases:
1. **Partial Overlap**: Tests when one interval starts before the other and ends within the other interval.
2. **Adjacent Intervals**: Tests when the end of the first interval is exactly the start of the second (no overlap).
3. **No Overlap**: Tests when the intervals are completely separate.
4. **Fully Contained**: Tests when one interval is entirely within another (should return `False` as per the spec).
5. **Identical Intervals**: Tests when the intervals are exactly the same (should return `False` as per the spec).
6. **Overlap at Start**: Tests when the second interval starts before the first and ends within the first interval.

These tests cover all critical paths and edge cases for the function's behavior.