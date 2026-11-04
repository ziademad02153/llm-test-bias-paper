def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 10) == []

def test_no_conflicting_reservations():
    reservations = [(1, 2, "A"), (3, 4, "B")]
    assert find_conflicting_reservations(reservations, 5, 10) == []

def test_conflicting_reservations():
    reservations = [(1, 10, "A"), (5, 15, "B"), (20, 25, "C")]
    assert find_conflicting_reservations(reservations, 1, 10) == ["A", "B"]

def test_edge_case_query_start_equals_query_end():
    reservations = [(1, 10, "A"), (5, 15, "B"), (20, 25, "C")]
    assert find_conflicting_reservations(reservations, 1, 1) == ["A", "B"]

def test_edge_case_empty_query_window():
    reservations = [(1, 10, "A"), (5, 15, "B"), (20, 25, "C")]
    assert find_conflicting_reservations(reservations, 10, 10) == []

def test_edge_case_query_window_out_of_bounds():
    reservations = [(1, 10, "A"), (5, 15, "B"), (20, 25, "C")]
    assert find_conflicting_reservations(reservations, -100, -50) == []