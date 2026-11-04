from typing import List, Tuple

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 10) == []

def test_no_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 2, 'A'), (3, 4, 'B')]
    assert find_conflicting_reservations(reservations, 5, 10) == []

def test_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A'), (5, 15, 'B'), (20, 25, 'C')]
    assert find_conflicting_reservations(reservations, 5, 15) == ['A', 'B']

def test_edge_case_query_start_equals_reservation_start():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A'), (5, 15, 'B')]
    assert find_conflicting_reservations(reservations, 1, 10) == ['A']

def test_edge_case_query_end_equals_reservation_end():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A'), (5, 15, 'B')]
    assert find_conflicting_reservations(reservations, 5, 10) == ['A', 'B']

def test_single_reservation():
    reservations: List[Tuple[int, int, str]] = [(1, 10, 'A')]
    assert find_conflicting_reservations(reservations, 1, 10) == ['A']