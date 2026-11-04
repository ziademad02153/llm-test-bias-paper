def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]

def test_compute_exponential_backoff_sequence_empty_input():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == []

def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 8.0]

def test_compute_exponential_backoff_sequence_factor():
    attempts = 5
    base = 2.0
    factor = 2.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [2.0, 4.0, 8.0, 16.0, 32.0]

def test_compute_exponential_backoff_sequence_max_value_factor():
    attempts = 5
    base = 2.0
    factor = 2.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [2.0, 4.0, 8.0, 8.0, 8.0]

def test_compute_exponential_backoff_sequence_negative_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = None
    with pytest.raises(ValueError):
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)

def test_compute_exponential_backoff_sequence_negative_factor():
    attempts = 5
    base = 2.0
    factor = -1.0
    max_value = None
    with pytest.raises(ValueError):
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)