def test_compute_fibonacci_backoff_sequence_standard_input():
    attempts = 5
    max_value = None
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert len(result) == attempts
    assert result == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_compute_fibonacci_backoff_sequence_with_max_value():
    attempts = 5
    max_value = 3.0
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert len(result) == attempts
    assert result == [1.0, 1.0, 2.0, 3.0, 3.0]

def test_compute_fibonacci_backoff_sequence_zero_attempts():
    attempts = 0
    max_value = None
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert len(result) == attempts
    assert result == []

def test_compute_fibonacci_backoff_sequence_negative_attempts():
    attempts = -1
    max_value = None
    try:
        compute_fibonacci_backoff_sequence(attempts, max_value)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        assert True

def test_compute_fibonacci_backoff_sequence_non_integer_attempts():
    attempts = 3.5
    max_value = None
    try:
        compute_fibonacci_backoff_sequence(attempts, max_value)
        assert False, "Expected TypeError for non-integer attempts"
    except TypeError:
        assert True

def test_compute_fibonacci_backoff_sequence_non_numeric_max_value():
    attempts = 5
    max_value = "max"
    try:
        compute_fibonacci_backoff_sequence(attempts, max_value)
        assert False, "Expected TypeError for non-numeric max_value"
    except TypeError:
        assert True