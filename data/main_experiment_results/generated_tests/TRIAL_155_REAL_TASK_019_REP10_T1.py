def test_empty_intervals():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 2)]) == [(1, 2)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 2), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 4), (5, 6)]) == [(1, 4), (5, 6)]

def test_unsorted_intervals():
    assert merge_overlapping_intervals([(5, 6), (1, 3), (2, 4)]) == [(1, 4), (5, 6)]

def test_equal_intervals():
    assert merge_overlapping_intervals([(1, 2), (1, 2)]) == [(1, 2)]

def test_large_intervals():
    assert merge_overlapping_intervals([(1, 10), (2, 5), (6, 8), (7, 9)]) == [(1, 10)]

def test_zero_length_intervals():
    assert merge_overlapping_intervals([(1, 1), (2, 2)]) == [(1, 1), (2, 2)]

def test_negative_intervals():
    assert merge_overlapping_intervals([(-5, 0), (-3, 2), (1, 3)]) == [(-5, 3)]