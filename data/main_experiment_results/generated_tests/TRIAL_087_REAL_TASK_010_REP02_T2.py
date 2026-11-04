def test_empty_reservations():
    assert find_conflicting_reservations([], 10, 20) == []

def test_no_conflicts():
    reservations = [(1, 5, "A"), (6, 10, "B"), (11, 15, "C")]
    assert find_conflicting_reservations(reservations, 16, 20) == []

def test_single_conflict():
    reservations = [(1, 5, "A"), (6, 10, "B"), (11, 15, "C")]
    assert find_conflicting_reservations(reservations, 4, 7) == ["A", "B"]

def test_multiple_conflicts():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C"), (8, 12, "D")]
    assert set(find_conflicting_reservations(reservations, 4, 9)) == {"A", "B", "C"}

def test_query_contains_reservation():
    reservations = [(5, 10, "A"), (15, 20, "B"), (25, 30, "C")]
    assert find_conflicting_reservations(reservations, 0, 100) == ["A", "B", "C"]

def test_reservation_contains_query():
    reservations = [(5, 20, "A"), (25, 40, "B")]
    assert find_conflicting_reservations(reservations, 10, 15) == ["A"]

def test_edge_case_query_touching_reservation():
    reservations = [(5, 10, "A"), (10, 15, "B")]
    assert find_conflicting_reservations(reservations, 9, 10) == ["A"]