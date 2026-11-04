def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 2)]) == [(1, 2)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 4)]) == [(1, 4)]

def test_nested_intervals():
    assert merge_overlapping_intervals([(1, 5), (2, 3), (4, 6)]) == [(1, 6)]

def test_unsorted_intervals():
    assert merge_overlapping_intervals([(2, 4), (1, 3), (5, 6)]) == [(1, 4), (5, 6)]