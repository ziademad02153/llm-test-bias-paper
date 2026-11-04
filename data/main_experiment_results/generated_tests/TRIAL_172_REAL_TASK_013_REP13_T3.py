def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals that overlap."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_start():
    """Test intersection with one interval having unbounded start (None)."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection with one interval having unbounded end (None)."""
    assert intersect_intervals(2, None, 3, 7) == (3, 7)

def test_intersect_no_overlap():
    """Test intervals that do not overlap (should return None)."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_both_unbounded():
    """Test intersection of two unbounded intervals (should return the bounded part)."""
    assert intersect_intervals(None, 5, 3, None) == (3, 5)

def test_intersect_identical_intervals():
    """Test intersection of identical intervals (should return the interval itself)."""
    assert intersect_intervals(2, 6, 2, 6) == (2, 6)