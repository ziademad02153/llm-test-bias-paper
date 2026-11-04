def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals with overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersecting two bounded intervals with no overlap
    assert intersect_intervals(1, 2, 3, 4) is None
    # Test intersecting two bounded intervals where one is contained within the other
    assert intersect_intervals(2, 8, 3, 5) == (3, 5)

def test_intersect_unbounded_start():
    # Test intersecting intervals where one has unbounded start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test intersecting intervals where both have unbounded start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)
    # Test no overlap when one interval ends before the other starts
    assert intersect_intervals(None, 2, 3, 4) is None

def test_intersect_unbounded_end():
    # Test intersecting intervals where one has unbounded end (None)
    assert intersect_intervals(3, None, 1, 5) == (3, 5)
    # Test intersecting intervals where both have unbounded end
    assert intersect_intervals(3, None, 1, None) == (3, None)
    # Test no overlap when one interval starts after the other ends
    assert intersect_intervals(6, None, 1, 4) is None

def test_intersect_fully_unbounded():
    # Test intersecting two fully unbounded intervals
    assert intersect_intervals(None, None, None, None) == (None, None)
    # Test intersecting fully unbounded with bounded
    assert intersect_intervals(None, None, 2, 4) == (2, 4)
    # Test intersecting fully unbounded with partially unbounded
    assert intersect_intervals(None, None, None, 5) == (None, 5)

def test_intersect_single_point():
    # Test intersecting single-point intervals (start == end)
    assert intersect_intervals(3, 3, 3, 3) == (3, 3)
    # Test single-point interval overlapping with a range
    assert intersect_intervals(3, 3, 1, 5) == (3, 3)
    # Test single-point interval not overlapping with a range
    assert intersect_intervals(3, 3, 4, 5) is None