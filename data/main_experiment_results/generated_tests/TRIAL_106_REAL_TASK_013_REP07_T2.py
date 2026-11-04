def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals with overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersecting two bounded intervals with no overlap
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_unbounded_start():
    # Test one interval with unbounded start (None) and another bounded
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test both intervals with unbounded start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test one interval with unbounded end (None) and another bounded
    assert intersect_intervals(3, None, 1, 5) == (3, 5)
    # Test both intervals with unbounded end
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test both intervals fully unbounded
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partial_overlap():
    # Test partial overlap where one interval is entirely within the other
    assert intersect_intervals(2, 6, 4, 5) == (4, 5)
    # Test partial overlap where intervals share a boundary
    assert intersect_intervals(2, 6, 6, 8) == (6, 6)

def test_intersect_no_overlap_edge():
    # Test intervals just touching but not overlapping (if considered non-inclusive)
    assert intersect_intervals(2, 5, 5, 8) == (5, 5)
    # Test intervals with no overlap and one unbounded
    assert intersect_intervals(2, 5, 6, None) is None