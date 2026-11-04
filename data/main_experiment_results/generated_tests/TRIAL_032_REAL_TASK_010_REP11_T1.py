import pytest

def test_find_conflicting_reservations_standard_input():
    reservations = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start = 2
    query_end = 5
    expected_conflicting_reservations = ['A', 'B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_empty_input():
    reservations = []
    query_start = 1
    query_end = 10
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_no_overlap():
    reservations = [(1, 3, 'A'), (5, 7, 'B')]
    query_start = 4
    query_end = 5
    expected_conflicting_reservations = ['B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_out_of_bounds():
    reservations = [(1, 3, 'A'), (5, 7, 'B')]
    query_start = 10
    query_end = 15
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_partially_out_of_bounds():
    reservations = [(1, 3, 'A'), (5, 7, 'B')]
    query_start = 0
    query_end = 2
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_equal_to_reservation():
    reservations = [(1, 3, 'A'), (5, 7, 'B')]
    query_start = 1
    query_end = 3
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations