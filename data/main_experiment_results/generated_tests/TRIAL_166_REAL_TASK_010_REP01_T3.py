Here's a comprehensive suite of unit tests for the `find_conflicting_reservations` function based on its specification:

```python
# Test 1: No overlapping reservations
def test_no_overlapping_reservations():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

# Test 2: Exact overlap with single reservation
def test_exact_overlap_single_reservation():
    reservations = [(5, 10, "X"), (15, 20, "Y")]
    assert find_conflicting_reservations(reservations, 5, 10) == ["X"]

# Test 3: Multiple overlapping reservations
def test_multiple_overlapping_reservations():
    reservations = [(1, 5, "A"), (3, 7, "B"), (6, 9, "C")]
    result = find_conflicting_reservations(reservations, 4, 8)
    assert set(result) == {"A", "B", "C"}  # Using set for unordered comparison

# Test 4: Edge case - empty reservations list
def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 5) == []

# Test 5: Partial overlap at boundaries
def test_partial_boundary_overlaps():
    reservations = [(10, 20, "P"), (20, 30, "Q"), (30, 40, "R")]
    assert find_conflicting_reservations(reservations, 15, 25) == ["P", "Q"]

# Test 6: Query contained within a reservation
def test_query_contained_within_reservation():
    reservations = [(100, 200, "Z"), (300, 400, "W")]
    assert find_conflicting_reservations(reservations, 150, 180) == ["Z"]
```

These tests cover:
1. Non-overlapping cases
2. Exact matches
3. Multiple overlaps
4. Empty input handling
5. Boundary conditions
6. Queries fully contained within reservations

The tests use simple `assert` statements and focus on the function's behavior according to its specification, without making assumptions about the implementation details.