Here is a comprehensive suite of unit tests for the `check_half_open_overlap` function:

```python
# Test case 1: Intervals overlap partially
def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test case 2: Intervals are adjacent (no overlap)
def test_adjacent_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 7) == False

# Test case 3: One interval fully contains the other (should return False as per spec)
def test_fully_contained():
    assert check_half_open_overlap(1, 10, 3, 7) == False

# Test case 4: Intervals do not overlap at all
def test_no_overlap():
    assert check_half_open_overlap(1, 5, 6, 7) == False

# Test case 5: Intervals are the same (should return False as per spec)
def test_same_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False

# Test case 6: One interval starts where the other ends (edge case)
def test_edge_case_adjacent():
    assert check_half_open_overlap(1, 5, 5, 10) == False
```

### Explanation of Test Cases:
1. **Partial Overlap**: Tests when intervals overlap partially (e.g., `[1,5)` and `[3,7)`).
2. **Adjacent No Overlap**: Tests when intervals are adjacent but do not overlap (e.g., `[1,5)` and `[5,7)`).
3. **Fully Contained**: Tests when one interval is fully contained within another (e.g., `[1,10)` and `[3,7)`), which should return `False` as per the specification.
4. **No Overlap**: Tests when intervals do not overlap at all (e.g., `[1,5)` and `[6,7)`).
5. **Same Intervals**: Tests when intervals are identical (e.g., `[1,5)` and `[1,5)`), which should return `False` as per the specification.
6. **Edge Case Adjacent**: Another edge case where one interval starts exactly where the other ends (similar to test case 2 but with different values).

These test cases cover standard inputs, edge cases, and the expected behavior as per the function's specification.