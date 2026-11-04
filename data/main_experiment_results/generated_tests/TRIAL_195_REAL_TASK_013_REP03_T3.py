def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals that overlap."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_non_overlapping_intervals():
    """Test intersection of two bounded intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_unbounded_left():
    """Test intersection with an unbounded left interval (None as start)."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_right():
    """Test intersection with an unbounded right interval (None as end)."""
    assert intersect_intervals(3, 7, 5, None) == (5, 7)

def test_intersect_both_unbounded():
    """Test intersection where both intervals are unbounded (None on both sides)."""
    assert intersect_intervals(None, 5, 3, None) == (3, 5)

def test_intersect_identical_intervals():
    """Test intersection of identical intervals."""
    assert intersect_intervals(2, 4, 2, 4) == (2, 4)