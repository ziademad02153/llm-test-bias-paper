def test_intersect_bounded_intervals():
    """Test intersection of two bounded intervals."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_start():
    """Test intersection with one interval having unbounded start."""
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_unbounded_end():
    """Test intersection with one interval having unbounded end."""
    assert intersect_intervals(2, 8, 4, None) == (4, 8)

def test_intersect_both_unbounded():
    """Test intersection with both intervals unbounded on opposite sides."""
    assert intersect_intervals(None, 5, 3, None) == (3, 5)

def test_no_intersection():
    """Test intervals that do not intersect."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_adjacent_intervals():
    """Test intervals that are adjacent but do not overlap."""
    assert intersect_intervals(1, 3, 3, 5) is None