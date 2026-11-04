def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 7, 9)
    assert result == []

def test_all_conflicts():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert set(result) == {"A", "B", "C"}

def test_partial_conflicts():
    reservations = [(1, 4, "A"), (3, 6, "B"), (5, 8, "C")]
    result = find_conflicting_reservations(reservations, 4, 7)
    assert set(result) == {"B", "C"}

def test_empty_reservations():
    reservations = []
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == []

def test_touching_intervals_no_conflict():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 3, 4)
    assert result == ["B"]

def test_query_interval_before_all_reservations():
    reservations = [(5, 7, "A"), (8, 10, "B")]
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == []