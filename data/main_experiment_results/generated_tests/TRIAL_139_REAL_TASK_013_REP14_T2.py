def test_intersect_bounded_intervals():
    # Test intersecting two bounded intervals
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    assert intersect_intervals(3, 7, 1, 5) == (3, 5)

def test_intersect_unbounded_start():
    # Test intersecting intervals where one has an unbounded start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    assert intersect_intervals(3, 7, None, 5) == (3, 5)

def test_intersect_unbounded_end():
    # Test intersecting intervals where one has an unbounded end (None)
    assert intersect_intervals(1, None, 3, 7) == (3, 7)
    assert intersect_intervals(3, 7, 1, None) == (3, 7)

def test_intersect_unbounded_both_ends():
    # Test intersecting intervals where both have unbounded starts or ends
    assert intersect_intervals(None, 5, None, 7) == (None, 5)
    assert intersect_intervals(1, None, 3, None) == (3, None)
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_no_intersection():
    # Test intervals that do not intersect
    assert intersect_intervals(1, 3, 5, 7) is None
    assert intersect_intervals(5, 7, 1, 3) is None

def test_intersect_point_intervals():
    # Test intervals that are single points (start == end)
    assert intersect_intervals(3, 3, 3, 3) == (3, 3)
    assert intersect_intervals(3, 3, 2, 5) == (3, 3)
    assert intersect_intervals(2, 5, 3, 3) == (3, 3)
    assert intersect_intervals(1, 2, 3, 3) is None