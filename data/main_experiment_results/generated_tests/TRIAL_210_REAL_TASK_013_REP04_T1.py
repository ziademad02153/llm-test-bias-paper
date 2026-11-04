def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_intersection():
    assert intersect_intervals(None, 5, 3, None) == (3, 5)
    assert intersect_intervals(1, None, None, 7) == (1, 7)
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_no_intersection():
    assert intersect_intervals(1, 3, 4, 7) is None

def test_empty_intersection():
    assert intersect_intervals(1, 1, 2, 2) is None

def test_unbounded_no_intersection():
    assert intersect_intervals(None, 3, 4, None) is None

def test_equal_intervals():
    assert intersect_intervals(1, 5, 1, 5) == (1, 5)
    assert intersect_intervals(None, 5, None, 5) == (None, 5)
    assert intersect_intervals(1, None, 1, None) == (1, None)
    assert intersect_intervals(None, None, None, None) == (None, None)