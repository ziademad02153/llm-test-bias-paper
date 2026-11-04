def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 7, 9)
    assert result == []

def test_exact_overlap():
    reservations = [(1, 5, "A"), (2, 4, "B")]
    result = find_conflicting_reservations(reservations, 2, 4)
    assert set(result) == {"A", "B"}

def test_partial_overlap():
    reservations = [(1, 5, "A"), (3, 6, "B"), (7, 9, "C")]
    result = find_conflicting_reservations(reservations, 4, 8)
    assert set(result) == {"A", "B", "C"}

def test_empty_reservations():
    result = find_conflicting_reservations([], 1, 3)
    assert result == []

def test_query_equals_reservation():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == ["A"]

def test_query_touching_no_overlap():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 3, 4)
    assert result == ["B"]