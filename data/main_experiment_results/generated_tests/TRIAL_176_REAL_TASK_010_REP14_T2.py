def test_no_conflicts():
    reservations = [(1, 2, "A"), (3, 4, "B"), (5, 6, "C")]
    result = find_conflicting_reservations(reservations, 7, 8)
    assert result == []

def test_all_conflicts():
    reservations = [(1, 4, "A"), (2, 5, "B"), (3, 6, "C")]
    result = find_conflicting_reservations(reservations, 1, 6)
    assert set(result) == {"A", "B", "C"}

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert set(result) == {"A", "B"}

def test_empty_reservations():
    reservations = []
    result = find_conflicting_reservations(reservations, 1, 2)
    assert result == []

def test_touching_intervals_no_conflict():
    reservations = [(1, 2, "A"), (2, 3, "B")]
    result = find_conflicting_reservations(reservations, 1, 2)
    assert result == ["A"]

def test_query_interval_inside_reservation():
    reservations = [(1, 10, "A"), (5, 6, "B")]
    result = find_conflicting_reservations(reservations, 4, 7)
    assert set(result) == {"A", "B"}