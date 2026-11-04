def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 2)]) == [(1, 2)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 2), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 4), (5, 6)]) == [(1, 4), (5, 6)]

def test_unsorted_intervals():
    assert merge_overlapping_intervals([(3, 4), (1, 2), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]

def test_equal_intervals():
    assert merge_overlapping_intervals([(1, 2), (1, 2)]) == [(1, 2)]

def test_invalid_input_type():
    try:
        merge_overlapping_intervals("invalid input")
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_invalid_interval_type():
    try:
        merge_overlapping_intervals([(1, 2), "invalid interval"])
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_invalid_interval_length():
    try:
        merge_overlapping_intervals([(1, 2), (3, 4, 5)])
        assert False, "Expected ValueError"
    except ValueError:
        pass