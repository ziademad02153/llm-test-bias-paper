from typing import List, Tuple

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 10) == []

def test_no_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 2, 'A'), (3, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 7, 8) == []

def test_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 2, 5) == ['A', 'B']

def test_edge_case_query_start_equals_reservation_start():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 1, 5) == ['A', 'B']

def test_edge_case_query_end_equals_reservation_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 1, 4) == ['A', 'B']

def test_single_reservation():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A')]
    assert find_conflicting_reservations(reservations, 2, 4) == ['A']