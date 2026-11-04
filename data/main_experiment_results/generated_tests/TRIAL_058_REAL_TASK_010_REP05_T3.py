# Test 1: Standard case with overlapping and non-overlapping reservations
def test_standard_case():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert sorted(result) == ["A", "B"]

# Test 2: No overlapping reservations
def test_no_overlaps():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 3, 4)
    assert result == []

# Test 3: Query exactly matches a reservation
def test_exact_match():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == ["A"]

# Test 4: Empty reservations list
def test_empty_reservations():
    result = find_conflicting_reservations([], 1, 3)
    assert result == []

# Test 5: Query overlaps all reservations
def test_query_overlaps_all():
    reservations = [(1, 3, "A"), (2, 4, "B"), (3, 5, "C")]
    result = find_conflicting_reservations(reservations, 0, 6)
    assert sorted(result) == ["A", "B", "C"]

# Test 6: Query is a single point (zero-length interval)
def test_zero_length_query():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 3, 3)
    assert result == []