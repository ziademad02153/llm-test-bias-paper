def test_intersect_bounded_intervals():
    # Test intersection of two bounded intervals that overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersection of two bounded intervals that do not overlap
    assert intersect_intervals(1, 3, 5, 7) is None
    # Test intersection where one interval is entirely within the other
    assert intersect_intervals(2, 8, 3, 6) == (3, 6)

def test_intersect_unbounded_start():
    # Test intersection where one interval has unbounded start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test intersection where both intervals have unbounded start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test intersection where one interval has unbounded end (None)
    assert intersect_intervals(3, None, 1, 7) == (3, 7)
    # Test intersection where both intervals have unbounded end
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test intersection where one interval is fully unbounded
    assert intersect_intervals(None, None, 1, 7) == (1, 7)
    # Test intersection where both intervals are fully unbounded
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_edge_cases():
    # Test intersection of single-point intervals
    assert intersect_intervals(3, 3, 3, 3) == (3, 3)
    # Test intersection where intervals are adjacent but do not overlap
    assert intersect_intervals(1, 3, 3, 5) is None
    # Test intersection where one interval is empty (start > end)
    assert intersect_intervals(5, 1, 2, 4) is None