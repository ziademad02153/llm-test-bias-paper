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

def test_find_conflicting_reservations_edge_case_query_start_equals_query_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 2
    query_end: int = 2
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_start_equals_zero():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 0
    query_end: int = 10
    expected_conflicting_reservations: List[str] = ['A', 'B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_query_end_equals_zero():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = 1
    query_end: int = 0
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_find_conflicting_reservations_edge_case_negative_query_start_and_query_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start: int = -10
    query_end: int = -1
    expected_conflicting_reservations: List[str] = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

test_find_conflicting_reservations_standard_input()
test_find_conflicting_reservations_empty_input()
test_find_conflicting_reservations_edge_case_query_start_equals_query_end()
test_find_conflicting_reservations_edge_case_query_start_equals_zero()
test_find_conflicting_reservations_edge_case_query_end_equals_zero()
test_find_conflicting_reservations_edge_case_negative_query_start_and_query_end()