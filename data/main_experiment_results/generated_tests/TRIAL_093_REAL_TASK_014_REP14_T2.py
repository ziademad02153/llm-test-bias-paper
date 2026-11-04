def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(5)
    expected = [1.0, 2.0, 4.0, 8.0, 16.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_with_custom_factor_and_base():
    """Test with custom factor and base."""
    result = compute_exponential_backoff_sequence(4, base=3.0, factor=0.5)
    expected = [0.5, 1.5, 4.5, 13.5]
    assert result == expected, f"Expected {expected}, got {result}"

def test_with_max_value():
    """Test with max_value limiting the sequence."""
    result = compute_exponential_backoff_sequence(5, max_value=10.0)
    expected = [1.0, 2.0, 4.0, 8.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_zero_attempts():
    """Test with zero attempts (edge case)."""
    result = compute_exponential_backoff_sequence(0)
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

def test_max_value_none():
    """Test with max_value=None (no upper bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    expected = [1.0, 2.0, 4.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_max_value_less_than_first_element():
    """Test when max_value is less than the first element."""
    result = compute_exponential_backoff_sequence(5, factor=2.0, max_value=1.0)
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"