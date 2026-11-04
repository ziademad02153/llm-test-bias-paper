def test_intersect_intervals_standard():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_intervals_unbounded():
    assert intersect_intervals(1, None, 3, 7) == (3, 7)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_intersect_intervals_empty():
    assert intersect_intervals(1, 5, None, None) is None
    assert intersect_intervals(None, None, 3, 7) is None
    assert intersect_intervals(None, None, None, None) is None

def test_intersect_intervals_no_intersection():
    assert intersect_intervals(1, 3, 4, 7) is None
    assert intersect_intervals(4, 7, 1, 3) is None

def test_intersect_intervals_equal():
    assert intersect_intervals(1, 5, 1, 5) == (1, 5)
    assert intersect_intervals(1, None, 1, None) == (1, None)
    assert intersect_intervals(None, 5, None, 5) == (None, 5)