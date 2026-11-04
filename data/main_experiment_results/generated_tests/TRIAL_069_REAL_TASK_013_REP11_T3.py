def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_start():
    """Test intersection with first interval having unbounded start."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection with second interval having unbounded end."""
    assert intersect_intervals(2, 6, 4, None) == (4, 6)

def test_intersect_no_overlap():
    """Test intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_both_unbounded():
    """Test intersection of two unbounded intervals."""
    assert intersect_intervals(None, 5, None, 7) == (None, 5)
    assert intersect_intervals(2, None, 1, None) == (2, None)

def test_intersect_point_intervals():
    """Test intersection of two point intervals (zero-width)."""
    assert intersect_intervals(3, 3, 3, 3) == (3, 3)
    assert intersect_intervals(3, 3, 4, 4) is None