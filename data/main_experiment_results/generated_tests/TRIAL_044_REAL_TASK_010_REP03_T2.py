def test_no_conflicts():
    reservations = [(1, 2, "A"), (3, 4, "B"), (5, 6, "C")]
    assert find_conflicting_reservations(reservations, 7, 8) == []

def test_all_conflicts():
    reservations = [(1, 4, "A"), (2, 5, "B"), (3, 6, "C")]
    result = find_conflicting_reservations(reservations, 1, 6)
    assert sorted(result) == ["A", "B", "C"]

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (2, 4, "B"), (5, 7, "C")]
    result = find_conflicting_reservations(reservations, 2, 6)
    assert sorted(result) == ["A", "B"]

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 2) == []

def test_exact_boundary():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 2, 4) == ["A", "B"]

def test_non_overlapping_but_adjacent():
    reservations = [(1, 2, "A"), (2, 3, "B")]
    assert find_conflicting_reservations(reservations, 1, 3) == ["A", "B"]