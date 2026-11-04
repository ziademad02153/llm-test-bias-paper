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
    assert result[0] <= result[1] <= result[2] <= result[3] <= result[4] <= max_value

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

def test_compute_exponential_backoff_sequence_max_value_bound():
    attempts = 10
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[-1] <= max_value

def test_compute_exponential_backoff_sequence_factor():
    attempts = 5
    base = 2.0
    factor = 1.5
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 3.0
    assert result[1] == 9.0
    assert result[2] == 27.0
    assert result[3] == 81.0
    assert result[4] == 243.0

def test_compute_exponential_backoff_sequence_base():
    attempts = 5
    base = 3.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result[0] == 3.0
    assert result[1] == 9.0
    assert result[2] == 27.0
    assert result[3] == 81.0
    assert result[4] == 243.0

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    result = compute_exponential_backoff_sequence(attempts, base, factor)
    assert len(result) == attempts
    assert result[0] == 2.0
    assert result[1] == 4.0
    assert result[2] == 8.0
    assert result[3] == 16.0
    assert result[4] == 32.0
```

Note that I've added a few more test cases to cover different scenarios, such as testing the `factor` and `base` parameters, as well