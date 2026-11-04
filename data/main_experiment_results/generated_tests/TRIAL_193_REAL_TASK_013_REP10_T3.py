def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_start():
    """Test intersection with first interval unbounded at start."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection with second interval unbounded at end."""
    assert intersect_intervals(2, 6, 4, None) == (4, 6)

def test_intersect_no_overlap():
    """Test intervals with no overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_fully_unbounded():
    """Test intersection of two fully unbounded intervals."""
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partial_unbounded_no_overlap():
    """Test partially unbounded intervals with no overlap."""
    assert intersect_intervals(None, 2, 3, None) is None