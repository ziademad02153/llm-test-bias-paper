from typing import List, Tuple

def test_empty_reservations():
    assert find_conflicting_reservations([], 1, 10) == []

def test_no_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 2, "A"), (3, 4, "B")]
    assert find_conflicting_reservations(reservations, 5, 6) == []

def test_conflicting_reservations():
    reservations: List[Tuple[int, int, str]] = [(1, 3, "A"), (2, 4, "B"), (5, 6, "C")]
    assert set(find_conflicting_reservations(reservations, 2, 4)) == {"A", "B"}

def test_edge_cases():
    reservations: List[Tuple[int, int, str]] = [(1, 10, "A")]
    assert find_conflicting_reservations(reservations, 0, 5) == ["A"]
    assert find_conflicting_reservations(reservations, 5, 15) == ["A"]
    assert find_conflicting_reservations(reservations, 1, 10) == ["A"]

def test_unordered_reservations():
    reservations: List[Tuple[int, int, str]] = [(5, 10, "A"), (1, 3, "B"), (2, 4, "C")]
    assert set(find_conflicting_reservations(reservations, 2, 4)) == {"B", "C"}