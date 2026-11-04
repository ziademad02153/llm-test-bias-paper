def test_standard_input():
    assert compute_fibonacci_backoff_sequence(5) == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_max_value():
    assert compute_fibonacci_backoff_sequence(10, max_value=8.0) == [1.0, 1.0, 2.0, 3.0, 5.0, 8.0]

def test_zero_attempts():
    assert compute_fibonacci_backoff_sequence(0) == []

def test_negative_attempts():
    try:
        compute_fibonacci_backoff_sequence(-1)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        assert True

def test_non_integer_attempts():
    try:
        compute_fibonacci_backoff_sequence(3.5)
        assert False, "Expected TypeError for non-integer attempts"
    except TypeError:
        assert True

def test_negative_max_value():
    try:
        compute_fibonacci_backoff_sequence(5, max_value=-1.0)
        assert False, "Expected ValueError for negative max_value"
    except ValueError:
        assert True