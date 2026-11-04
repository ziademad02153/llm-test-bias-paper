from typing import List, Tuple

def test_standard_input():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 7, 'C')]
    query_start, query_end = 2, 5
    expected_conflicting_reservations = ['A', 'B']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_empty_input():
    reservations: List[Tuple[int, int, str]] = []
    query_start, query_end = 1, 10
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_edge_case_no_overlap():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (5, 7, 'B')]
    query_start, query_end = 4, 5
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_edge_case_full_overlap():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A')]
    query_start, query_end = 1, 10
    expected_conflicting_reservations = ['A']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_edge_case_query_out_of_bounds():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A')]
    query_start, query_end = 20, 30
    expected_conflicting_reservations = []
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

def test_multiple_overlapping_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 5, 'A'), (2, 6, 'B'), (3, 7, 'C')]
    query_start, query_end = 1, 8
    expected_conflicting_reservations = ['A', 'B', 'C']
    assert find_conflicting_reservations(reservations, query_start, query_end) == expected_conflicting_reservations

test_standard_input()
test_empty_input()
test_edge_case_no_overlap()
test_edge_case_full_overlap()
test_edge_case_query_out_of_bounds()
test_multiple_overlapping_reservations()