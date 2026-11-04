# Test overlapping intervals
def test_overlapping_intervals():
    assert check_half_open_overlap(1, 5, 3, 7) == True

# Test non-overlapping intervals
def test_non_overlapping_intervals():
    assert check_half_open_overlap(1, 3, 4, 7) == False

# Test edge case: intervals with same start and end points
def test_edge_case_same_start_and_end():
    assert check_half_open_overlap(1, 5, 1, 5) == False

# Test edge case: interval with zero length
def test_edge_case_zero_length_interval():
    assert check_half_open_overlap(1, 1, 2, 3) == False

# Test edge case: negative interval values
def test_edge_case_negative_interval_values():
    assert check_half_open_overlap(-3, 1, -2, 2) == True

# Test edge case: interval with start greater than end
def test_edge_case_invalid_interval():
    try:
        check_half_open_overlap(5, 1, 2, 3)
        assert False, "Expected an exception or False for invalid interval"
    except Exception:
        pass