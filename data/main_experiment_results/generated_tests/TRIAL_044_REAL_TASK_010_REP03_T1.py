from typing import List, Tuple

def test_find_conflicting_reservations_standard_input():
    reservations: List[Tuple[int, int, str]] = [(1, 5, 'A'), (3, 7, 'B'), (6, 10, 'C')]
    query_start: int = 4
    query_end: int = 9
    expected_conflicting_reservations: List[str] = ['A', 'B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_empty_input():
    reservations: List[Tuple[int, int, str]] = []
    query_start: int = 1
    query_end: int = 10
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_no_overlap():
    reservations: List[Tuple[int, int, str]] = [(1, 5, 'A'), (6, 10, 'B')]
    query_start: int = 11
    query_end: int = 15
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_larger_than_all_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 5, 'A'), (6, 10, 'B')]
    query_start: int = 0
    query_end: int = 15
    expected_conflicting_reservations: List[str] = ['A', 'B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_smaller_than_all_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A')]
    query_start: int = 3
    query_end: int = 7
    expected_conflicting_reservations: List[str] = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_query_window_equal_to_reservation():
    reservations: List[Tuple[int, int, str]] = [(1, 5, 'A')]
    query_start: int = 1
    query_end: int = 5
    expected_conflicting_reservations: List[str] = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations