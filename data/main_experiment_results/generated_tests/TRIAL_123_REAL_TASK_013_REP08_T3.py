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

def test_intersect_fully_unbounded():
    """Test intersection where both intervals are unbounded."""
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partially_unbounded_no_overlap():
    """Test partially unbounded intervals with no overlap."""
    assert intersect_intervals(None, 2, 3, None) is None