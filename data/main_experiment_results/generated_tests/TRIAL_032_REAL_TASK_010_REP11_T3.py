Here's a comprehensive suite of unit tests for the `find_conflicting_reservations` function based on its specification:

```python
# Test 1: No overlapping reservations
def test_no_overlaps():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

# Test 2: Single overlapping reservation
def test_single_overlap():
    reservations = [(1, 5, "A"), (6, 8, "B"), (10, 12, "C")]
    assert find_conflicting_reservations(reservations, 2, 4) == ["A"]

# Test 3: Multiple overlapping reservations
def test_multiple_overlaps():
    reservations = [(1, 5, "A"), (3, 7, "B"), (4, 8, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert set(result) == {"A", "B", "C"}  # Using set for unordered comparison

# Test 4: Query exactly matches reservation
def test_exact_match():
    reservations = [(5, 10, "X"), (12, 15, "Y")]
    assert find_conflicting_reservations(reservations, 5, 10) == ["X"]

# Test 5: Empty reservations list
def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 5) == []

# Test 6: Adjacent but non-overlapping reservations
def test_adjacent_non_overlapping():
    reservations = [(1, 2, "A"), (2, 3, "B"), (3, 4, "C")]
    assert find_conflicting_reservations(reservations, 2, 3) == ["B"]
```

These tests cover:
1. No overlaps case
2. Single overlap case
3. Multiple overlaps case
4. Exact match case
5. Empty input case
6. Edge case with adjacent intervals

The tests verify the function's behavior with both standard and edge case inputs, while maintaining independence from the implementation details (using only the function's specification).