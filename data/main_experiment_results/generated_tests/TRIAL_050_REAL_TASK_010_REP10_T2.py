def test_no_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B")]
    assert find_conflicting_reservations(reservations, 7, 9) == []

def test_all_conflicts():
    reservations = [(1, 3, "A"), (2, 5, "B"), (4, 6, "C")]
    result = find_conflicting_reservations(reservations, 1, 6)
    assert sorted(result) == ["A", "B", "C"]

def test_partial_conflicts():
    reservations = [(1, 3, "A"), (4, 6, "B"), (7, 9, "C")]
    result = find_conflicting_reservations(reservations, 2, 8)
    assert sorted(result) == ["A", "B", "C"]

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 3) == []

def test_edge_case_query_equals_reservation():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 3, 5) == ["B"]

def test_non_overlapping_but_adjacent():
    reservations = [(1, 3, "A"), (3, 5, "B")]
    assert find_conflicting_reservations(reservations, 4, 6) == ["B"]