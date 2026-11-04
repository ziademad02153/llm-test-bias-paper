from typing import List, Tuple

def test_find_conflicting_reservations_standard_input():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start, query_end = 2, 5
    expected_conflicting_reservations = ['A', 'B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_empty_input():
    reservations: List[Tuple[int, int, str]] = []
    query_start, query_end = 1, 10
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_no_overlap():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (4, 6, 'B')]
    query_start, query_end = 7, 10
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_full_overlap():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A')]
    query_start, query_end = 1, 10
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_start_equals_reservation_start():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A')]
    query_start, query_end = 1, 10
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_end_equals_reservation_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A')]
    query_start, query_end = 0, 3
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations