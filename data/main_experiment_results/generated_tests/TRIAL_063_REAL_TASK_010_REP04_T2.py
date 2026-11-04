def test_empty_reservations():
    """Test with no reservations should return empty list."""
    assert find_conflicting_reservations([], 10, 20) == []

def test_no_conflicts():
    """Test with reservations that don't conflict with query window."""
    reservations = [(1, 5, "A"), (6, 9, "B"), (10, 15, "C")]
    assert find_conflicting_reservations(reservations, 16, 20) == []

def test_single_conflict():
    """Test with a single reservation conflicting with query window."""
    reservations = [(10, 20, "A"), (30, 40, "B")]
    assert find_conflicting_reservations(reservations, 15, 25) == ["A"]

def test_multiple_conflicts():
    """Test with multiple reservations conflicting with query window."""
    reservations = [(5, 15, "A"), (10, 20, "B"), (15, 25, "C")]
    result = find_conflicting_reservations(reservations, 12, 18)
    assert sorted(result) == sorted(["A", "B"])

def test_query_equals_reservation():
    """Test when query window exactly matches a reservation."""
    reservations = [(10, 20, "A"), (20, 30, "B")]
    assert find_conflicting_reservations(reservations, 10, 20) == ["A"]

def test_overlapping_reservations():
    """Test with overlapping reservations and query window."""
    reservations = [(5, 15, "A"), (10, 20, "B"), (25, 35, "C")]
    result = find_conflicting_reservations(reservations, 12, 22)
    assert sorted(result) == sorted(["A", "B"])