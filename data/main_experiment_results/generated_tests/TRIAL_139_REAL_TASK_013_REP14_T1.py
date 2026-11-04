def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_start():
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)

def test_unbounded_end():
    assert intersect_intervals(1, None, 3, 7) == (3, 7)

def test_unbounded_both():
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_no_intersection():
    assert intersect_intervals(1, 2, 3, 4) is None

def test_equal_intervals():
    assert intersect_intervals(1, 5, 1, 5) == (1, 5)