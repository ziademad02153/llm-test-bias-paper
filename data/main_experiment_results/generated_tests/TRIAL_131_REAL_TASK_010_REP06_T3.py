Here's a comprehensive suite of unit tests for the `find_conflicting_reservations` function based on its specification:

```python
# Test 1: No overlapping reservations
def test_no_overlaps():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

# Test 2: Exact overlap with one reservation
def test_exact_overlap():
    reservations = [(1, 5, "A"), (6, 10, "B")]
    assert find_conflicting_reservations(reservations, 1, 5) == ["A"]

# Test 3: Partial overlaps with multiple reservations
def test_partial_overlaps():
    reservations = [(1, 5, "A"), (3, 7, "B"), (6, 10, "C")]
    result = find_conflicting_reservations(reservations, 4, 8)
    assert sorted(result) == ["A", "B", "C"]

# Test 4: Query window contained within a reservation
def test_query_contained():
    reservations = [(1, 10, "A"), (15, 20, "B")]
    assert find_conflicting_reservations(reservations, 3, 7) == ["A"]

# Test 5: Empty reservations list
def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 5) == []

# Test 6: Adjacent but non-overlapping reservations
def test_adjacent_non_overlapping():
    reservations = [(1, 5, "A"), (5, 10, "B")]
    assert find_conflicting_reservations(reservations, 4, 5) == ["A"]
```

These tests cover:
1. No overlaps with query window
2. Exact match with a reservation
3. Multiple partial overlaps
4. Query window fully contained within a reservation
5. Empty input case
6. Edge case with adjacent but non-overlapping intervals

The tests verify the function's behavior with various interval relationships while maintaining independence from the implementation details (using only the function's specification).