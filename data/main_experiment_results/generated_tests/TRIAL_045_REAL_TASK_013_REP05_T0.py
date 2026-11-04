def test_intersect_intervals_standard():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    assert intersect_intervals(1, 5, 6, 7) is None

def test_intersect_intervals_unbounded():
    assert intersect_intervals(1, None, 3, None) == (3, None)
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_intervals_edge_cases():
    assert intersect_intervals(1, 1, 1, 1) == (1, 1)
    assert intersect_intervals(1, 5, None, None) == (1, 5)
    assert intersect_intervals(None, None, 1, 5) == (1, 5)
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_intervals_no_intersection():
    assert intersect_intervals(1, 2, 3, 4) is None
    assert intersect_intervals(1, None, 2, None) is None

def test_intersect_intervals_invalid_inputs():
    try:
        intersect_intervals('a', 5, 1, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        intersect_intervals(1, 5, [1, 7], 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass