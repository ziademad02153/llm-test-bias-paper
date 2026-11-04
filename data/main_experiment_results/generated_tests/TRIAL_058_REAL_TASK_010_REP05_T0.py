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
    query_start = 4
    query_end = 4
    expected_result = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_edge_case_query_window_start_equal():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 1
    query_end = 5
    expected_result = ['Reservation 1', 'Reservation 2']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_edge_case_query_window_end_equal():
    reservations = [(1, 3, 'Reservation 1'), (2, 4, 'Reservation 2')]
    query_start = 0
    query_end = 3
    expected_result = ['Reservation 1', 'Reservation 2']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_result

def test_find_conflicting_reservations_invalid_input():
    reservations = None
    query_start = 1
    query_end = 10
    try:
        find_conflicting_reservations(reservations, query_start, query_end)
        assert False, "Expected TypeError"
    except TypeError:
        assert True