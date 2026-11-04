def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_left_intersection():
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_unbounded_right_intersection():
    assert intersect_intervals(1, None, 3, 7) == (3, None)

def test_unbounded_both_intersection():
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_no_intersection():
    assert intersect_intervals(1, 2, 3, 4) is None

def test_empty_intervals():
    assert intersect_intervals(None, None, None, None) == (None, None)
    assert intersect_intervals(1, 2, None, None) is None
    assert intersect_intervals(None, None, 1, 2) is None