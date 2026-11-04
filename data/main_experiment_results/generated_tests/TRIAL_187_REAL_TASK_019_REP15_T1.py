def test_empty_intervals():
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

def test_large_intervals():
    assert merge_overlapping_intervals([(1, 100), (50, 200), (150, 300)]) == [(1, 300)]

test_empty_intervals()
test_single_interval()
test_non_overlapping_intervals()
test_overlapping_intervals()
test_unsorted_intervals()
test_equal_intervals()
test_large_intervals()