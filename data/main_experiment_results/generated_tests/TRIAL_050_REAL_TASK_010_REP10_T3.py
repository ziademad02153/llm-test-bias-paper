Here is a comprehensive suite of unit tests for the `find_conflicting_reservations` function based on its specification:

```python
# Test 1: No overlapping reservations
def test_no_overlapping_reservations():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

# Test 2: All reservations overlap with query
def test_all_reservations_overlap():
    reservations = [(1, 4, "A"), (2, 5, "B"), (3, 6, "C")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert sorted(result) == ["A", "B", "C"]

# Test 3: Some reservations overlap with query
def test_some_reservations_overlap():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert sorted(result) == ["A", "B"]

# Test 4: Empty reservations list
def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

# Test 5: Query exactly matches reservation
def test_query_matches_reservation():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    assert find_conflicting_reservations(reservations, 1, 3) == ["A"]

# Test 6: Edge case - zero-length query
def test_zero_length_query():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 3, 3) == []
```

These tests cover:
1. No overlaps (empty result)
2. All reservations overlapping
3. Partial overlaps
4. Empty input list
5. Exact match of query to reservation
6. Zero-length query interval (edge case)

The tests use simple `assert` statements and cover the main scenarios while keeping each test focused on one specific behavior. The tests assume the function is already imported/available in the test namespace as specified.