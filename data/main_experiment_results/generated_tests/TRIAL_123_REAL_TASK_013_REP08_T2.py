def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals that overlap."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_start():
    """Test intersection where one interval has unbounded start (None)."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection where one interval has unbounded end (None)."""
    assert intersect_intervals(1, None, 3, 7) == (3, 7)

def test_intersect_no_overlap():
    """Test intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_both_unbounded():
    """Test intersection where both intervals are unbounded."""
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partial_unbounded():
    """Test intersection where one interval is unbounded and the other is bounded."""
    assert intersect_intervals(None, 10, 5, None) == (5, 10)