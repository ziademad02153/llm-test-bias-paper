def test_find_conflicting_reservations_standard_input():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2'), (5, 7, 'Reservation 3')]
    query_start = 2
    query_end = 5
    expected_result = ['Reservation 1', 'Reservation 2', 'Reservation 3']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_empty_input():
    reservations = []
    query_start = 1
    query_end = 10
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_edge_case_query_window():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 0
    query_end = 0
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_edge_case_query_window_out_of_bounds():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 10
    query_end = 20
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_query_window_partially_overlapping():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2'), (5, 7, 'Reservation 3')]
    query_start = 3
    query_end = 6
    expected_result = ['Reservation 2', 'Reservation 3']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result