def test_compute_fibonacci_backoff_sequence_standard_input():
    attempts = 5
    max_value = None
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)

def test_compute_fibonacci_backoff_sequence_max_value():
    attempts = 5
    max_value = 10.0
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(x <= max_value for x in result)

def test_compute_fibonacci_backoff_sequence_zero_attempts():
    attempts = 0
    max_value = None
    result = compute_fibonacci_backoff_sequence(attempts, max_value)
    assert result == []

def test_compute_fibonacci_backoff_sequence_negative_attempts():
    attempts = -1
    max_value = None
    try:
        compute_fibonacci_backoff_sequence(attempts, max_value)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        pass

def test_compute_fibonacci_backoff_sequence_non_numeric_max_value():
    attempts = 5
    max_value = "non-numeric"
    try:
        compute_fibonacci_backoff_sequence(attempts, max_value)
        assert False, "Expected TypeError for non-numeric max_value"
    except TypeError:
        pass