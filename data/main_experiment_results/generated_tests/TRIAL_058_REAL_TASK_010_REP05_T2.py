def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    result = find_conflicting_reservations(reservations, 10, 12)
    assert result == []

def test_all_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (3, 5, "C")]
    result = find_conflicting_reservations(reservations, 1, 5)
    assert set(result) == {"A", "B", "C"}

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert set(result) == {"A", "B"}

def test_empty_reservations():
    reservations = []
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == []

def test_edge_case_query_touching_reservation_end():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 2, 3)
    assert result == ["A"]

def test_query_inside_reservation():
    reservations = [(1, 10, "A"), (2, 5, "B")]
    result = find_conflicting_reservations(reservations, 3, 4)
    assert set(result) == {"A", "B"}