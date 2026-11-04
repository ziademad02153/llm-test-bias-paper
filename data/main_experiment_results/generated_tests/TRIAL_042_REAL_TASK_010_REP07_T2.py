def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

def test_all_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (3, 5, "C")]
    result = find_conflicting_reservations(reservations, 1, 5)
    assert set(result) == {"A", "B", "C"}

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 4, 6)
    assert set(result) == {"B", "C"}

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

def test_touching_intervals_no_conflict():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 3, 4) == ["B"]

def test_query_interval_contains_reservation():
    reservations = [(2, 4, "A"), (5, 7, "B")]
    assert find_conflicting_reservations(reservations, 1, 8) == ["A", "B"]