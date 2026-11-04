def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == factor * (base ** 1)
    assert result[1] == factor * (base ** 2)
    assert result[2] == factor * (base ** 3)
    assert result[3] == factor * (base ** 4)
    assert result[4] == factor * (base ** 5)
    assert all(delay <= max_value for delay in result)

def test_compute_exponential_backoff_sequence_empty_input():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_max_value_bound():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(delay <= max_value for delay in result)

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    result = compute_exponential_backoff_sequence(attempts, base, factor)
    assert len(result) == attempts
    assert all(delay > 0 for delay in result)

def test_compute_exponential_backoff_sequence_negative_attempts():
    attempts = -1
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_invalid_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = "invalid"
    try:
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        assert False, "Expected ValueError"
    except ValueError:
        pass