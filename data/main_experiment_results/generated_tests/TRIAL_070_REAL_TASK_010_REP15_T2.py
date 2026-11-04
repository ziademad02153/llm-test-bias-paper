def test_empty_reservations():
    assert find_conflicting_reservations([], 10, 20) == []

def test_no_conflicts():
    reservations = [(1, 5, "A"), (6, 10, "B"), (11, 15, "C")]
    assert find_conflicting_reservations(reservations, 16, 20) == []

def test_single_conflict():
    reservations = [(1, 5, "A"), (6, 10, "B"), (11, 15, "C")]
    assert find_conflicting_reservations(reservations, 4, 8) == ["A", "B"]

def test_multiple_conflicts():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C"), (8, 12, "D")]
    assert set(find_conflicting_reservations(reservations, 4, 9)) == {"A", "B", "C", "D"}

def test_query_contains_all_reservations():
    reservations = [(1, 5, "A"), (6, 10, "B"), (11, 15, "C")]
    assert set(find_conflicting_reservations(reservations, 0, 20)) == {"A", "B", "C"}

def test_query_exact_match():
    reservations = [(10, 20, "A"), (15, 25, "B")]
    assert find_conflicting_reservations(reservations, 10, 20) == ["A", "B"]