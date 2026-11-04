def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_intersection():
    assert intersect_intervals(None, 5, 3, None) == (3, 5)

def test_empty_intersection():
    assert intersect_intervals(1, 5, 7, 10) is None

def test_unbounded_empty_intersection():
    assert intersect_intervals(None, 5, 7, None) is None

def test_equal_unbounded_intersection():
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_single_point_intersection():
    assert intersect_intervals(5, 5, 5, 5) == (5, 5)