def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    assert find_conflicting_reservations(reservations, 10, 12) == []

def test_all_conflicts():
    reservations = [(1, 4, "A"), (2, 5, "B"), (3, 6, "C")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert sorted(result) == ["A", "B", "C"]

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert sorted(result) == ["A", "B"]

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

def test_query_inside_reservation():
    reservations = [(1, 10, "A"), (5, 8, "B")]
    result = find_conflicting_reservations(reservations, 6, 7)
    assert sorted(result) == ["A", "B"]

def test_query_exact_match():
    reservations = [(1, 5, "A"), (6, 10, "B")]
    assert find_conflicting_reservations(reservations, 1, 5) == ["A"]