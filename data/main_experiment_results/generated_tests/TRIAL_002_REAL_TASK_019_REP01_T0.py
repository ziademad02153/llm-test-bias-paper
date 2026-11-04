def test_empty_input():
    assert merge_overlapping_intervals([]) == []

def test_non_overlapping_intervals():
    intervals = [(1, 3), (5, 7), (9, 11)]
    expected_output = [(1, 3), (5, 7), (9, 11)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_overlapping_intervals():
    intervals = [(1, 4), (3, 6), (8, 10), (9, 12)]
    expected_output = [(1, 6), (8, 12)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_edge_cases():
    intervals = [(1, 1), (2, 3), (3, 4), (5, 5)]
    expected_output = [(1, 1), (2, 4), (5, 5)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_unsorted_intervals():
    intervals = [(5, 7), (1, 3), (9, 11), (2, 4)]
    expected_output = [(1, 4), (5, 7), (9, 11)]
    assert merge_overlapping_intervals(intervals) == expected_output

def test_invalid_input_type():
    try:
        merge_overlapping_intervals("invalid input")
        assert False, "Expected TypeError"
    except TypeError:
        pass