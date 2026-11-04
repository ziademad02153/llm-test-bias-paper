def test_standard_inputs():
    """Test standard inputs with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2
    assert result == expected

def test_custom_base_and_factor():
    """Test with custom base and factor."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=2.0)
    expected = [2.0, 6.0, 18.0]  # 2 * 3^0, 2 * 3^1, 2 * 3^2
    assert result == expected

def test_max_value_constraint():
    """Test max_value constraint."""
    result = compute_exponential_backoff_sequence(5, max_value=10.0)
    expected = [1.0, 2.0, 4.0, 8.0]  # 2^0, 2^1, 2^2, 2^3 (2^4=16 > 10)
    assert result == expected

def test_zero_attempts():
    """Test edge case with zero attempts."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_max_value_none():
    """Test max_value=None (no upper bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    expected = [1.0, 2.0, 4.0]
    assert result == expected

def test_all_values_exceed_max_value():
    """Test case where all values exceed max_value."""
    result = compute_exponential_backoff_sequence(3, max_value=0.5)
    assert result == []