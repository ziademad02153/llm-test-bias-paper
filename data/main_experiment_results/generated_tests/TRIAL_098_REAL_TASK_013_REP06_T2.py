def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals with overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersecting two bounded intervals without overlap
    assert intersect_intervals(1, 3, 4, 6) is None

def test_intersect_unbounded_start():
    # Test intersecting an unbounded start interval with a bounded interval
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test intersecting two unbounded start intervals
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test intersecting an unbounded end interval with a bounded interval
    assert intersect_intervals(3, None, 1, 5) == (3, 5)
    # Test intersecting two unbounded end intervals
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test intersecting two fully unbounded intervals
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partial_overlap():
    # Test intervals with partial overlap
    assert intersect_intervals(2, 6, 4, 8) == (4, 6)
    # Test intervals where one is entirely within the other
    assert intersect_intervals(1, 10, 3, 7) == (3, 7)

def test_intersect_edge_cases():
    # Test intervals with single-point overlap
    assert intersect_intervals(1, 3, 3, 5) == (3, 3)
    # Test intervals with no overlap (adjacent)
    assert intersect_intervals(1, 2, 2, 3) is None