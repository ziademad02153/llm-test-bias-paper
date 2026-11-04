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
    """Test intersection with both intervals unbounded."""
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_edge_case_touching():
    """Test edge case where intervals touch but do not overlap."""
    assert intersect_intervals(1, 5, 5, 10) is None