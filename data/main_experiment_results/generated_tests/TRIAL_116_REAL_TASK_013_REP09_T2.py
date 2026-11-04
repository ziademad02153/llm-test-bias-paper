def test_intersect_intervals_basic():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    assert intersect_intervals(1, 5, 6, 8) is None

def test_intersect_intervals_unbounded():
    assert intersect_intervals(None, 5, 3, None) == (3, 5)
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_intervals_edge_cases():
    assert intersect_intervals(1, 1, 1, 1) == (1, 1)
    assert intersect_intervals(1, 5, 5, 7) == (5, 5)
    assert intersect_intervals(1, 5, 0, 2) == (1, 2)

def test_intersect_intervals_no_overlap():
    assert intersect_intervals(1, 3, 4, 6) is None
    assert intersect_intervals(10, 20, 1, 5) is None

def test_intersect_intervals_partial_unbounded():
    assert intersect_intervals(None, 10, 5, None) == (5, 10)
    assert intersect_intervals(1, None, None, 7) == (1, 7)