def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals with overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersecting two bounded intervals without overlap
    assert intersect_intervals(1, 2, 3, 4) is None
    # Test intersecting two bounded intervals touching at a point
    assert intersect_intervals(1, 3, 3, 5) == (3, 3)

def test_intersect_unbounded_start():
    # Test one interval with unbounded start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test both intervals with unbounded start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test one interval with unbounded end (None)
    assert intersect_intervals(3, None, 1, 7) == (3, 7)
    # Test both intervals with unbounded end
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test one fully unbounded interval
    assert intersect_intervals(None, None, 2, 4) == (2, 4)
    # Test both fully unbounded intervals
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_empty_result():
    # Test intervals that don't intersect
    assert intersect_intervals(1, 2, 3, 4) is None
    # Test one interval completely before the other
    assert intersect_intervals(1, 2, 2, 4) == (2, 2)