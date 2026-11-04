def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(x <= max_value for x in result)
    assert result[0] == factor * (base ** 0)
    assert result[-1] == factor * (base ** attempts)

def test_compute_exponential_backoff_sequence_empty_inputs():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_max_value_bound():
    attempts = 10
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x <= max_value for x in result)

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 10
    base = 2.0
    factor = 1.0
    result = compute_exponential_backoff_sequence(attempts, base, factor)
    assert all(x > 0 for x in result)

def test_compute_exponential_backoff_sequence_negative_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x >= 0 for x in result)

def test_compute_exponential_backoff_sequence_zero_factor():
    attempts = 5
    base = 2.0
    factor = 0.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x == 0 for x in result)