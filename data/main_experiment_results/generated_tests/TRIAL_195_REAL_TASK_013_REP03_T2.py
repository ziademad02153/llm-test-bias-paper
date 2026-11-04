def test_intersect_intervals_basic():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_intersect_intervals_unbounded_start():
    assert intersect_intervals(None, 10, 5, 15) == (5, 10)

def test_intersect_intervals_unbounded_end():
    assert intersect_intervals(2, None, 1, 8) == (2, 8)

def test_intersect_intervals_no_intersection():
    assert intersect_intervals(1, 3, 4, 6) is None

def test_intersect_intervals_unbounded_both():
    assert intersect_intervals(None, None, 5, 10) == (5, 10)

def test_intersect_intervals_edge_case():
    assert intersect_intervals(5, 5, 5, 5) == (5, 5)