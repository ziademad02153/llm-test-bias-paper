def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    assert find_conflicting_reservations(reservations, 7, 9) == []

def test_all_conflicts():
    reservations = [(1, 5, "A"), (2, 6, "B"), (3, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 4)
    assert sorted(result) == ["A", "B", "C"]

def test_partial_overlaps():
    reservations = [(1, 4, "A"), (3, 6, "B"), (5, 8, "C")]
    result = find_conflicting_reservations(reservations, 2, 7)
    assert sorted(result) == ["A", "B", "C"]

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

def test_exact_match():
    reservations = [(10, 20, "X"), (15, 25, "Y")]
    assert sorted(find_conflicting_reservations(reservations, 15, 20)) == ["X", "Y"]

def test_touching_intervals_non_overlapping():
    reservations = [(1, 2, "A"), (2, 3, "B")]
    assert find_conflicting_reservations(reservations, 2, 3) == ["B"]