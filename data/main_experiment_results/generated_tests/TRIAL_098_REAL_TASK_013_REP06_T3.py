def test_intersect_intervals_basic():
    """Test basic intersection of two intervals."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_intervals_no_overlap():
    """Test intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_intervals_unbounded():
    """Test intervals with unbounded endpoints."""
    assert intersect_intervals(1, None, 3, 7) == (3, 7)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_intersect_intervals_fully_unbounded():
    """Test fully unbounded intervals."""
    assert intersect_intervals(None, None, 3, 7) == (3, 7)
    assert intersect_intervals(1, 5, None, None) == (1, 5)

def test_intersect_intervals_edge_case_single_point():
    """Test intervals that intersect at a single point."""
    assert intersect_intervals(1, 3, 3, 5) == (3, 3)
    assert intersect_intervals(3, 5, 1, 3) == (3, 3)

def test_intersect_intervals_one_interval_inside_another():
    """Test when one interval is completely inside another."""
    assert intersect_intervals(2, 4, 1, 5) == (2, 4)
    assert intersect_intervals(1, 5, 2, 4) == (2, 4)