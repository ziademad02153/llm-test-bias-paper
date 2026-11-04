def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_single_interval():
    assert merge_overlapping_intervals([(1, 2)]) == [(1, 2)]

def test_non_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]

def test_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (2, 4)]) == [(1, 4)]

def test_partially_overlapping_intervals():
    assert merge_overlapping_intervals([(1, 3), (3, 5)]) == [(1, 5)]

def test_unsorted_intervals():
    assert merge_overlapping_intervals([(3, 5), (1, 3)]) == [(1, 5)]

def test_large_intervals():
    assert merge_overlapping_intervals([(1, 100), (50, 200), (150, 250)]) == [(1, 250)]

def test_equal_intervals():
    assert merge_overlapping_intervals([(1, 2), (1, 2)]) == [(1, 2)]

def test_zero_length_intervals():
    assert merge_overlapping_intervals([(1, 1), (2, 2)]) == [(1, 1), (2, 2)]

def test_negative_intervals():
    assert merge_overlapping_intervals([(-5, 0), (-3, 2)]) == [(-5, 2)]

def test_large_numbers():
    assert merge_overlapping_intervals([(1000000, 2000000), (1500000, 2500000)]) == [(1000000, 2500000)]