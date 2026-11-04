def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (5, 7), (9, 11)]
    assert merge_overlapping_intervals(intervals) == [(1, 3), (5, 7), (9, 11)]

def test_overlapping_intervals():
    intervals = [(1, 4), (3, 6), (8, 10), (9, 12)]
    assert merge_overlapping_intervals(intervals) == [(1, 6), (8, 12)]

def test_adjacent_intervals():
    intervals = [(1, 3), (3, 5), (6, 8), (8, 10)]
    assert merge_overlapping_intervals(intervals) == [(1, 5), (6, 10)]

def test_single_interval():
    intervals = [(1, 10)]
    assert merge_overlapping_intervals(intervals) == [(1, 10)]

def test_invalid_input():
    try:
        merge_overlapping_intervals([(1, 2), (3, 4), 'invalid'])
        assert False, "Expected a TypeError"
    except TypeError:
        pass