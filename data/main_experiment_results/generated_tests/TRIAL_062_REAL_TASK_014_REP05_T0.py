def test_compute_exponential_backoff_sequence_standard_input():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_empty_attempts():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= max_value for x in result)

def test_compute_exponential_backoff_sequence_factor_zero():
    attempts = 5
    base = 2.0
    factor = 0.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)

def test_compute_exponential_backoff_sequence_base_zero():
    attempts = 5
    base = 0.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(isinstance(x, float) for x in result)
    assert all(0.0 <= x <= float('inf') for x in result)
```

Note: The `assert` statements are used to verify the behavior of the `compute_exponential_backoff_sequence` function. The `test_...()` functions are used to organize the test cases.