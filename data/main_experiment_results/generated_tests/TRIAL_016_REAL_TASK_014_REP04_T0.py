def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_empty_inputs():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_bounds():
    attempts = 1
    base = 2.0
    factor = 1.0
    max_value = 1.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 1
    assert result[0] == 1.0

def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x <= max_value for x in result)

def test_compute_exponential_backoff_sequence_factor():
    attempts = 5
    base = 2.0
    factor = 2.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x > 0.0 for x in result)

def test_compute_exponential_backoff_sequence_base():
    attempts = 5
    base = 1.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert all(x > 0.0 for x in result)