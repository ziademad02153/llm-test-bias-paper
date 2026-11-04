def test_standard_input():
    assert compute_fibonacci_backoff_sequence(5) == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_max_value():
    assert compute_fibonacci_backoff_sequence(5, max_value=5.0) == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_max_value_bounded():
    assert compute_fibonacci_backoff_sequence(10, max_value=5.0) == [1.0, 1.0, 2.0, 3.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

def test_zero_attempts():
    assert compute_fibonacci_backoff_sequence(0) == []

def test_negative_attempts():
    try:
        compute_fibonacci_backoff_sequence(-1)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        pass

def test_non_integer_attempts():
    try:
        compute_fibonacci_backoff_sequence(3.5)
        assert False, "Expected TypeError for non-integer attempts"
    except TypeError:
        pass