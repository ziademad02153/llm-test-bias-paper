Here's a comprehensive suite of unit tests for the `find_conflicting_reservations` function based on its specification:

```python
# Test 1: No overlapping reservations
def test_no_overlaps():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

# Test 2: Single overlapping reservation
def test_single_overlap():
    reservations = [(1, 5, "A"), (6, 8, "B"), (10, 12, "C")]
    assert find_conflicting_reservations(reservations, 3, 6) == ["A"]

# Test 3: Multiple overlapping reservations
def test_multiple_overlaps():
    reservations = [(1, 5, "A"), (3, 7, "B"), (4, 8, "C")]
    result = find_conflicting_reservations(reservations, 4, 6)
    assert sorted(result) == sorted(["A", "B", "C"])

# Test 4: Query exactly matches reservation
def test_exact_match():
    reservations = [(5, 10, "X"), (12, 15, "Y")]
    assert find_conflicting_reservations(reservations, 5, 10) == ["X"]

# Test 5: Empty reservations list
def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 5) == []

# Test 6: Query overlaps with reservation at boundary
def test_boundary_overlap():
    reservations = [(10, 20, "Z"), (25, 30, "W")]
    assert find_conflicting_reservations(reservations, 15, 20) == ["Z"]
```

These tests cover:
1. No overlaps case
2. Single overlap case
3. Multiple overlaps case (with unordered result check)
4. Exact match case
5. Empty input case
6. Boundary condition (end time matching)

The tests use simple assert statements and cover the main functionality while including edge cases. Note that for multiple overlaps (Test 3), we sort the results before comparison since the order isn't specified in the function's contract.