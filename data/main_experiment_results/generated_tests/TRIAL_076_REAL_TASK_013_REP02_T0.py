def test_intersect_intervals_standard():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    assert intersect_intervals(1, 5, 6, 7) is None
    assert intersect_intervals(1, 5, None, 7) == (1, 5)

def test_intersect_intervals_unbounded():
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    assert intersect_intervals(1, None, 3, 7) == (3, None)
    assert intersect_intervals(None, None, 3, 7) == (3, 7)
    assert intersect_intervals(1, 5, None, None) == (1, 5)

def test_intersect_intervals_edge_cases():
    assert intersect_intervals(1, 1, 1, 1) == (1, 1)
    assert intersect_intervals(1, 5, 1, 5) == (1, 5)
    assert intersect_intervals(None, None, None, None) == (None, None)
    assert intersect_intervals(1, None, None, None) == (1, None)
    assert intersect_intervals(None, 5, None, 5) == (None, 5)

def test_intersect_intervals_invalid_inputs():
    try:
        intersect_intervals('a', 5, 3, 7)
        assert False, "Expected TypeError for invalid input type"
    except TypeError:
        pass

    try:
        intersect_intervals(5, 'a', 3, 7)
        assert False, "Expected TypeError for invalid input type"
    except TypeError:
        pass

    try:
        intersect_intervals(5, 3, 7, 'a')
        assert False, "Expected TypeError for invalid input type"
    except TypeError:
        pass

    try:
        intersect_intervals(5, 3, 'a', 7)
        assert False, "Expected TypeError for invalid input type"
    except TypeError:
        pass