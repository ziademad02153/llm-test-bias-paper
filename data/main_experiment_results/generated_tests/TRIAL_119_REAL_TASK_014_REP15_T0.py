def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 1.0
    assert result[1] == 2.0
    assert result[2] == 4.0
    assert result[3] == 8.0
    assert result[4] == 16.0
    assert result[0] <= max_value
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_empty_input():
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
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 1.0
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_factor_non_default():
    attempts = 5
    base = 2.0
    factor = 1.5
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 1.0
    assert result[1] == 3.0
    assert result[2] == 9.0
    assert result[3] == 27.0
    assert result[4] == 81.0

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 1.0
    assert result[1] == 2.0
    assert result[2] == 4.0
    assert result[3] == 8.0
    assert result[4] == 16.0