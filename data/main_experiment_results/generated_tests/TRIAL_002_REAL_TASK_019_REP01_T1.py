def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 2)]) == [(1, 2)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 2), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 4), (5, 7)]) == [(1, 4), (5, 7)]

def test_adjacent_intervals():
    assert merge_overlapping_intervals([(1, 2), (2, 3), (3, 4)]) == [(1, 4)]

def test_unsorted_intervals():
    assert merge_overlapping_intervals([(3, 5), (1, 2), (4, 6)]) == [(1, 2), (3, 6)]