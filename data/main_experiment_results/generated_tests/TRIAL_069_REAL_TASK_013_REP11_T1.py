def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_start_intersection():
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_unbounded_end_intersection():
    assert intersect_intervals(1, None, 3, 7) == (3, 7)

def test_unbounded_both_intersection():
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_no_intersection():
    assert intersect_intervals(1, 5, 6, 7) is None

def test_unbounded_intersection():
    assert intersect_intervals(None, None, None, None) == (None, None)