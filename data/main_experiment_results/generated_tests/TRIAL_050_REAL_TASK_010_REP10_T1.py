from typing import List, Tuple

def test_find_conflicting_reservations_standard_input():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 2
    query_end: int = 5
    expected_conflicting_reservations: List[str] = ['A', 'B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_empty_input():
    reservations: List[Tuple[int, int, str]] = []
    query_start: int = 1
    query_end: int = 10
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_window_outside_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 10
    query_end: int = 15
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_window_partially_overlapping():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 3
    query_end: int = 6
    expected_conflicting_reservations: List[str] = ['B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_window_equal_to_reservation():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 2
    query_end: int = 4
    expected_conflicting_reservations: List[str] = ['B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_window_zero_length():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 2
    query_end: int = 2
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations