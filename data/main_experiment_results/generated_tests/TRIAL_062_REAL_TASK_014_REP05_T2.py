def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]

def test_with_custom_factor_and_base():
    """Test with custom factor and base."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=2.0)
    assert result == [2.0, 6.0, 18.0]

def test_with_max_value():
    """Test with max_value limiting the sequence."""
    result = compute_exponential_backoff_sequence(5, max_value=10.0)
    assert result == [1.0, 2.0, 4.0, 8.0]

def test_zero_attempts():
    """Test with zero attempts (edge case)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_max_value_none():
    """Test with max_value=None (no limit)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    assert result == [1.0, 2.0, 4.0]

def test_max_value_less_than_first_element():
    """Test when max_value is less than the first element."""
    result = compute_exponential_backoff_sequence(3, factor=2.0, max_value=1.0)
    assert result == []