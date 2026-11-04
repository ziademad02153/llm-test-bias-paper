def test_standard_input():
    reservations = [(1, 5, 'A'), (3, 7, 'B'), (8, 10, 'C')]
    query_start = 2
    query_end = 9
    expected_conflicting_reservations = ['A', 'B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_empty_input():
    reservations = []
    query_start = 1
    query_end = 10
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_no_conflicting_reservations():
    reservations = [(1, 5, 'A'), (8, 10, 'B')]
    query_start = 6
    query_end = 7
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_query_window_out_of_bounds():
    reservations = [(1, 5, 'A'), (8, 10, 'B')]
    query_start = 15
    query_end = 20
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_query_window_partially_out_of_bounds():
    reservations = [(1, 5, 'A'), (8, 10, 'B')]
    query_start = 0
    query_end = 3
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_query_window_exactly_matches_reservation():
    reservations = [(1, 5, 'A'), (8, 10, 'B')]
    query_start = 1
    query_end = 5
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations