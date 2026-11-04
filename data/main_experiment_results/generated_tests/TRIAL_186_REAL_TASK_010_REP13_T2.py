def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    result = find_conflicting_reservations(reservations, 7, 9)
    assert result == []

def test_all_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B")]
    result = find_conflicting_reservations(reservations, 0, 5)
    assert set(result) == {"A", "B"}

def test_partial_overlap():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert set(result) == {"A", "B"}

def test_empty_reservations():
    reservations = []
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == []

def test_exact_match():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 1, 3)
    assert result == ["A"]

def test_touching_intervals_no_overlap():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    result = find_conflicting_reservations(reservations, 3, 4)
    assert result == ["B"]