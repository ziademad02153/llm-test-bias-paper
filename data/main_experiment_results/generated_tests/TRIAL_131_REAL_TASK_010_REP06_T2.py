def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 7, 9)
    assert result == []

def test_single_conflict():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert result == ["A"]

def test_multiple_conflicts():
    reservations = [(1, 5, "A"), (2, 4, "B"), (3, 6, "C")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert sorted(result) == ["A", "B", "C"]

def test_empty_reservations():
    reservations = []
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == []

def test_exact_match():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == ["A"]

def test_query_contains_reservation():
    reservations = [(2, 4, "A"), (5, 7, "B")]
    result = find_conflicting_reservations(reservations, 1, 8)
    assert sorted(result) == ["A", "B"]