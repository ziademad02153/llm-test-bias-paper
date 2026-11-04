def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 2.0
    assert result[1] == 4.0
    assert result[2] == 8.0
    assert result[3] == 16.0
    assert result[4] == 32.0
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_empty_input():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_single_attempt():
    attempts = 1
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 1
    assert result[0] == 2.0

def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_negative_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 2.0
    assert result[1] == 4.0
    assert result[2] == 8.0
    assert result[3] == 16.0
    assert result[4] == 32.0
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_zero_factor():
    attempts = 5
    base = 2.0
    factor = 0.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 0.0
    assert result[1] == 0.0
    assert result[2] == 0.0
    assert result[3] == 0.0
    assert result[4] == 0.0
    assert result[-1] <= max_value