def test_standard_input():
    reservations = [(1, 5, "Reservation 1"), (3, 7, "Reservation 2"), (8, 10, "Reservation 3")]
    query_start = 2
    query_end = 6
    expected_output = ["Reservation 1", "Reservation 2"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_empty_reservations():
    reservations = []
    query_start = 1
    query_end = 10
    expected_output = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_query_window_outside_reservations():
    reservations = [(1, 5, "Reservation 1"), (8, 10, "Reservation 3")]
    query_start = 6
    query_end = 7
    expected_output = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_query_window_partially_overlapping():
    reservations = [(1, 5, "Reservation 1"), (3, 7, "Reservation 2"), (8, 10, "Reservation 3")]
    query_start = 4
    query_end = 9
    expected_output = ["Reservation 1", "Reservation 2", "Reservation 3"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_query_window_equal_to_reservation():
    reservations = [(1, 5, "Reservation 1"), (8, 10, "Reservation 3")]
    query_start = 1
    query_end = 5
    expected_output = ["Reservation 1"]
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_query_window_empty():
    reservations = [(1, 5, "Reservation 1"), (8, 10, "Reservation 3")]
    query_start = 1
    query_end = 1
    expected_output = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output