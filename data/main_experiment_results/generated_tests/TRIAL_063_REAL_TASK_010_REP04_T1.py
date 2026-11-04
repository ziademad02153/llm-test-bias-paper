from typing import List, Tuple

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 10) == []

def test_no_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 2, 'A'), (3, 4, 'B')]
    assert find_conflicting_reservations(reservations, 5, 6) == []

def test_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 2, 5) == ['A', 'B']

def test_query_window_at_start():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 1, 2) == ['A']

def test_query_window_at_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 3, 4) == ['B']

def test_query_window_beyond_end():
    reservations: List[Tuple[int, int, str]] = [(1, 3, 'A'), (2, 4, 'B'), (5, 6, 'C')]
    assert find_conflicting_reservations(reservations, 7, 8) == []

test_empty_reservations()
test_no_conflicting_reservations()
test_conflicting_reservations()
test_query_window_at_start()
test_query_window_at_end()
test_query_window_beyond_end()