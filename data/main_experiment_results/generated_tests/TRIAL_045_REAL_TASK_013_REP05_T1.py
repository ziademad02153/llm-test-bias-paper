def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

def test_unbounded_intersection():
    assert intersect_intervals(None, 5, 3, None) == (3, 5)
    assert intersect_intervals(1, None, None, 7) == (1, 7)
    assert intersect_intervals(None, None, 3, 7) == (3, 7)

def test_no_intersection():
    assert intersect_intervals(1, 3, 4, 7) is None

def test_edge_cases():
    assert intersect_intervals(None, None, None, None) == (None, None)
    assert intersect_intervals(1, 1, 1, 1) == (1, 1)
    assert intersect_intervals(1, None, 1, None) == (1, None)

def test_invalid_input():
    try:
        intersect_intervals('a', 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass