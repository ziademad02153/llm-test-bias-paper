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
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_bounds():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= max_value for x in result)

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_max_value_non_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= max_value for x in result)

def test_compute_exponential_backoff_sequence_invalid_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = None
    try:
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        assert False
    except ValueError:
        assert True

def test_compute_exponential_backoff_sequence_invalid_factor():
    attempts = 5
    base = 2.0
    factor = -1.0
    max_value = None
    try:
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        assert False
    except ValueError:
        assert True

def test_compute_exponential_backoff_sequence_invalid_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = -100.0
    try:
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        assert False
    except ValueError:
        assert True