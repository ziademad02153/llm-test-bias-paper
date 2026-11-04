def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    assert find_conflicting_reservations(reservations, 7, 9) == []

def test_exact_overlap():
    reservations = [(1, 5, "A"), (2, 4, "B")]
    assert set(find_conflicting_reservations(reservations, 2, 4)) == {"A", "B"}

def test_partial_overlap():
    reservations = [(1, 5, "A"), (3, 7, "B"), (6, 8, "C")]
    assert set(find_conflicting_reservations(reservations, 4, 6)) == {"A", "B"}

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

def test_query_equals_reservation():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 1, 3) == ["A"]

def test_multiple_non_overlapping():
    reservations = [(1, 2, "A"), (3, 4, "B"), (5, 6, "C")]
    assert find_conflicting_reservations(reservations, 2, 5) == ["B"]