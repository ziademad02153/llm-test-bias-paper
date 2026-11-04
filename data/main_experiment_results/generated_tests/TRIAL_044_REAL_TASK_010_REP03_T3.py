def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    assert find_conflicting_reservations(reservations, 7, 9) == []

def test_all_conflicts():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 5)
    assert sorted(result) == ["A", "B", "C"]

def test_partial_overlap():
    reservations = [(1, 4, "A"), (3, 6, "B"), (5, 8, "C")]
    result = find_conflicting_reservations(reservations, 4, 7)
    assert sorted(result) == ["B", "C"]

def test_empty_input():
    assert find_conflicting_reservations([], 1, 5) == []

def test_exact_match():
    reservations = [(10, 20, "X"), (20, 30, "Y")]
    assert find_conflicting_reservations(reservations, 10, 20) == ["X"]

def test_touching_intervals_no_conflict():
    reservations = [(1, 2, "A"), (2, 3, "B")]
    assert find_conflicting_reservations(reservations, 1, 3) == ["A", "B"]