def test_find_conflicting_reservations_standard_input():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2'), (5, 6, 'Reservation 3')]
    query_start = 2
    query_end = 4
    expected_output = ['Reservation 1', 'Reservation 2']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_find_conflicting_reservations_empty_input():
    reservations = []
    query_start = 1
    query_end = 2
    expected_output = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_find_conflicting_reservations_edge_case_query_window_outside_reservations():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 5
    query_end = 6
    expected_output = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_find_conflicting_reservations_edge_case_query_window_partially_overlapping():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 3
    query_end = 4
    expected_output = ['Reservation 2']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_find_conflicting_reservations_edge_case_query_window_equal_to_reservation():
    reservations = [(1, 3, 'Reservation 1')]
    query_start = 1
    query_end = 3
    expected_output = ['Reservation 1']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output

def test_find_conflicting_reservations_edge_case_query_window_zero_length():
    reservations = [(1, 3, 'Reservation 1')]
    query_start = 2
    query_end = 2
    expected_output = ['Reservation 1']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_output