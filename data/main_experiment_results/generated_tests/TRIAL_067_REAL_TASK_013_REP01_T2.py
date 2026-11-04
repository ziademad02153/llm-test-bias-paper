def test_intersect_bounded_intervals():
    # Test two bounded intervals that overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test two bounded intervals that do not overlap
    assert intersect_intervals(1, 2, 3, 4) is None
    # Test two bounded intervals where one is within the other
    assert intersect_intervals(2, 8, 3, 5) == (3, 5)

def test_intersect_unbounded_start():
    # Test one interval with unbounded start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test both intervals with unbounded start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test one interval with unbounded end (None)
    assert intersect_intervals(3, None, 1, 5) == (3, 5)
    # Test both intervals with unbounded end
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_no_overlap_unbounded():
    # Test intervals with no overlap, one unbounded
    assert intersect_intervals(None, 2, 3, None) is None
    # Test intervals with no overlap, both unbounded in opposite directions
    assert intersect_intervals(None, 1, 2, None) is None

def test_intersect_fully_unbounded():
    # Test both intervals fully unbounded
    assert intersect_intervals(None, None, None, None) == (None, None)
    # Test one fully unbounded and one partially bounded
    assert intersect_intervals(None, None, 1, None) == (1, None)

def test_intersect_single_point():
    # Test intervals intersecting at a single point
    assert intersect_intervals(1, 1, 1, 1) == (1, 1)
    # Test intervals that "touch" but do not overlap
    assert intersect_intervals(1, 2, 2, 3) == (2, 2)
    # Test intervals that do not touch
    assert intersect_intervals(1, 2, 3, 4) is None