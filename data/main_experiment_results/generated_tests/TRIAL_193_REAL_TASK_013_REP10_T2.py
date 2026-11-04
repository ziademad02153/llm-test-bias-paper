def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals with overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersecting two bounded intervals without overlap
    assert intersect_intervals(1, 3, 5, 7) is None

def test_intersect_unbounded_start():
    # Test intersecting an interval with unbounded start (None) with a bounded interval
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test intersecting two intervals with unbounded start (None)
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test intersecting an interval with unbounded end (None) with a bounded interval
    assert intersect_intervals(3, None, 1, 7) == (3, 7)
    # Test intersecting two intervals with unbounded end (None)
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test intersecting two fully unbounded intervals
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_partially_unbounded():
    # Test intersecting partially unbounded intervals
    assert intersect_intervals(None, 10, 5, None) == (5, 10)
    assert intersect_intervals(2, None, None, 8) == (2, 8)

def test_no_intersection_edge_cases():
    # Test edge cases where intervals just touch or don't intersect
    assert intersect_intervals(1, 2, 2, 3) == (2, 2)  # Touching at a point
    assert intersect_intervals(1, 2, 3, 4) is None  # No intersection