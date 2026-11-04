def test_find_conflicting_reservations_standard_input():
    reservations = [(1, 5, "Reservation 1"), (3, 7, "Reservation 2"), (8, 10, "Reservation 3")]
    query_start = 2
    query_end = 6
    expected_result = ["Reservation 1", "Reservation 2"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_empty_input():
    reservations = []
    query_start = 1
    query_end = 10
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_no_overlap():
    reservations = [(1, 5, "Reservation 1"), (6, 10, "Reservation 2")]
    query_start = 11
    query_end = 15
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_query_window_at_bounds():
    reservations = [(1, 5, "Reservation 1"), (5, 10, "Reservation 2")]
    query_start = 1
    query_end = 10
    expected_result = ["Reservation 1", "Reservation 2"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_query_window_exceeds_bounds():
    reservations = [(1, 5, "Reservation 1"), (5, 10, "Reservation 2")]
    query_start = 0
    query_end = 11
    expected_result = ["Reservation 1", "Reservation 2"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result