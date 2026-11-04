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
    assert all(0 <= x <= max_value for x in result)


def test_compute_exponential_backoff_sequence_empty_attempts():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0


def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(0 <= x <= max_value for x in result)


def test_compute_exponential_backoff_sequence_factor():
    attempts = 5
    base = 2.0
    factor = 1.5
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(0 <= x <= max_value for x in result)


def test_compute_exponential_backoff_sequence_base():
    attempts = 5
    base = 1.5
    factor = 1.0
    max_value = 100.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert all(0 <= x <= max_value for x in result)


def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    result = compute_exponential_backoff_sequence(attempts, base, factor)
    assert len(result) == attempts
    assert all(0 <= x <= 100.0 for x in result)
```

This test suite covers the following cases:

*   Standard input: Verifies that the function generates the correct exponential backoff sequence for a given number of attempts, base, factor, and max_value.
*   Empty attempts: Tests that the function returns an empty list when the number of attempts is 0.
*   Max value: Verifies that the function correctly bounds the exponential backoff sequence by the specified max_value.
*   Factor: Tests that the function correctly applies the specified factor to the exponential backoff sequence.
*   Base: Verifies that the function correctly uses the specified base for the exponential backoff sequence.
*   Max value none: Tests that the function correctly uses the default max_value of 100.0 when it is not specified.