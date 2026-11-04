def test_intersect_intervals_basic():
    """Test basic intersection of two intervals."""
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_intervals_no_overlap():
    """Test intervals that do not overlap."""
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_intervals_unbounded():
    """Test intervals with unbounded endpoints."""
    assert intersect_intervals(1, None, 3, 7) == (3, 7)
    assert intersect_intervals(None, 5, 1, 3) == (1, 3)

def test_intersect_intervals_identical():
    """Test identical intervals."""
    assert intersect_intervals(2, 6, 2, 6) == (2, 6)

def test_intersect_intervals_edge_case_empty():
    """Test edge case where one interval is empty (s == e)."""
    assert intersect_intervals(3, 3, 1, 5) is None

def test_intersect_intervals_both_unbounded():
    """Test both intervals are unbounded."""
    assert intersect_intervals(None, None, None, None) == (None, None)