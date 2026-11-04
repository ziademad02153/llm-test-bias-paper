# Test case 1: Intersection of two bounded intervals
def test_bounded_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

# Test case 2: Intersection of two unbounded intervals
def test_unbounded_intersection():
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

# Test case 3: Intersection of a bounded and an unbounded interval
def test_mixed_intersection():
    assert intersect_intervals(1, 5, None, 7) == (1, 5)

# Test case 4: Intersection of two intervals with no overlap
def test_no_overlap():
    assert intersect_intervals(1, 5, 6, 7) is None

# Test case 5: Intersection of two intervals with one being a single point
def test_single_point():
    assert intersect_intervals(5, 5, 5, 7) == (5, 5)

# Test case 6: Intersection of two intervals with one being empty (None, None)
def test_empty_interval():
    assert intersect_intervals(None, None, 1, 5) is None