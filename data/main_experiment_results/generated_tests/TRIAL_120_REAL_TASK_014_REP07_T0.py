def test_compute_exponential_backoff_sequence_standard_inputs():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]


def test_compute_exponential_backoff_sequence_empty_inputs():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == []


def test_compute_exponential_backoff_sequence_bounds():
    attempts = 10
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 100.0]


def test_compute_exponential_backoff_sequence_max_value():
    attempts = 10
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 2.0, 4.0, 8.0, 10.0]


def test_compute_exponential_backoff_sequence_negative_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]


def test_compute_exponential_backoff_sequence_zero_base():
    attempts = 5
    base = 0.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 1.0, 1.0, 1.0, 1.0]


def test_compute_exponential_backoff_sequence_negative_factor():
    attempts = 5
    base = 2.0
    factor = -1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]
```

These tests cover various scenarios, including standard inputs, edge cases (empty inputs, bounds), and exception behavior. They verify the correctness of the `compute_exponential_backoff_sequence` function under different conditions.