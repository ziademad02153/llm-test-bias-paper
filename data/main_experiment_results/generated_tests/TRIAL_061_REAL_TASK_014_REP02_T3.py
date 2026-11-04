Here's a comprehensive suite of unit tests for the `compute_exponential_backoff_sequence` function based on its specification:

```python
def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]  # 2**0, 2**1, 2**2

def test_custom_factor():
    """Test with custom factor."""
    result = compute_exponential_backoff_sequence(3, factor=0.5)
    assert result == [0.5, 1.0, 2.0]  # 0.5 * (2**0), 0.5 * (2**1), 0.5 * (2**2)

def test_max_value_bound():
    """Test sequence bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, max_value=3.0)
    assert result == [1.0, 2.0, 3.0, 3.0, 3.0]  # 2**2=4 gets capped to 3.0

def test_zero_attempts():
    """Test edge case with zero attempts."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_non_default_base():
    """Test with non-default base value."""
    result = compute_exponential_backoff_sequence(3, base=3.0)
    assert result == [1.0, 3.0, 9.0]  # 3**0, 3**1, 3**2

def test_negative_factor():
    """Test with negative factor (should still work mathematically)."""
    result = compute_exponential_backoff_sequence(3, factor=-1.0)
    assert result == [-1.0, -2.0, -4.0]  # -1 * (2**0), -1 * (2**1), -1 * (2**2)
```

These tests cover:
1. The standard case with default parameters
2. Custom factor values
3. Maximum value bounding
4. Edge case with zero attempts
5. Non-default base values
6. Negative factors (mathematically valid case)

The tests verify the function's behavior against the specification without making any assumptions about implementation details.