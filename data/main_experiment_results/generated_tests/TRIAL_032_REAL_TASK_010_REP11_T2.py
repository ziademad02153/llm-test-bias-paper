# Test 1: Standard case with overlapping reservations
def test_standard_case():
    reservations = [(1, 5, 'A'), (3, 7, 'B'), (6, 10, 'C')]
    query_start, query_end = 4, 8
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert sorted(result) == ['B', 'C']

# Test 2: No overlapping reservations
def test_no_overlap():
    reservations = [(1, 3, 'A'), (4, 6, 'B'), (7, 9, 'C')]
    query_start, query_end = 10, 12
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == []

# Test 3: Empty reservations list
def test_empty_reservations():
    reservations = []
    query_start, query_end = 1, 5
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == []

# Test 4: Query interval completely within a reservation
def test_query_within_reservation():
    reservations = [(1, 10, 'A'), (15, 20, 'B')]
    query_start, query_end = 2, 4
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == ['A']

# Test 5: Query interval overlaps multiple reservations
def test_multiple_overlaps():
    reservations = [(1, 5, 'A'), (4, 8, 'B'), (7, 10, 'C'), (9, 12, 'D')]
    query_start, query_end = 6, 11
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert sorted(result) == ['B', 'C', 'D']

# Test 6: Query interval exactly matches a reservation
def test_query_exact_match():
    reservations = [(1, 5, 'A'), (6, 10, 'B')]
    query_start, query_end = 6, 10
    result = find_conflicting_reservations(reservations, query_start, query_end)
    assert result == ['B']