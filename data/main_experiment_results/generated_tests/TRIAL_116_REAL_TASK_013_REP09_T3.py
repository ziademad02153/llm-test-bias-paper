def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals that overlap."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_non_overlapping_intervals():
    """Test intersection of two bounded intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_unbounded_start():
    """Test intersection with an unbounded start (None) on first interval."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection with an unbounded end (None) on second interval."""
    assert intersect_intervals(2, 6, 4, None) == (4, 6)

def test_intersect_both_unbounded():
    """Test intersection where both intervals are unbounded (infinite)."""
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partially_unbounded_no_overlap():
    """Test intersection where one interval is unbounded but no overlap exists."""
    assert intersect_intervals(None, 2, 4, 6) is None