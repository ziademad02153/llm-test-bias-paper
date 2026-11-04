# Test 1: No overlapping reservations
def test_no_overlapping_reservations():
    reservations = [(1, 2, "A"), (3, 4, "B"), (5, 6, "C")]
    query_start, query_end = 7, 8
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == []

# Test 2: All reservations overlap
def test_all_reservations_overlap():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C")]
    query_start, query_end = 2, 6
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert set(result) == {"A", "B", "C"}

# Test 3: Partial overlapping reservations
def test_partial_overlapping_reservations():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    query_start, query_end = 2, 6
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert set(result) == {"A", "B"}

# Test 4: Empty reservations list
def test_empty_reservations_list():
    reservations = []
    query_start, query_end = 1, 2
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == []

# Test 5: Query interval completely inside a reservation
def test_query_inside_reservation():
    reservations = [(1, 10, "A"), (11, 20, "B")]
    query_start, query_end = 2, 5
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == ["A"]

# Test 6: Query interval overlaps with multiple reservations
def test_query_overlaps_multiple_reservations():
    reservations = [(1, 5, "A"), (4, 8, "B"), (7, 10, "C")]
    query_start, query_end = 6, 9
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert set(result) == {"B", "C"}