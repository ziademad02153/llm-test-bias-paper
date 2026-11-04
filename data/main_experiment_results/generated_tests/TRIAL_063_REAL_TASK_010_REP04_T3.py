def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 7, 9)
    assert result == []

def test_exact_overlap():
    reservations = [(1, 5, "A"), (2, 4, "B")]
    result = find_conflicting_reservations(reservations, 2, 4)
    assert set(result) == {"A", "B"}

def test_partial_overlap():
    reservations = [(1, 5, "A"), (3, 7, "B"), (6, 8, "C")]
    result = find_conflicting_reservations(reservations, 4, 6)
    assert set(result) == {"A", "B"}

def test_empty_reservations():
    result = find_conflicting_reservations([], 1, 3)
    assert result == []

def test_query_touching_boundary():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 2, 3)
    assert result == ["A"]

def test_query_inside_reservation():
    reservations = [(1, 10, "A"), (2, 4, "B")]
    result = find_conflicting_reservations(reservations, 3, 5)
    assert set(result) == {"A", "B"}