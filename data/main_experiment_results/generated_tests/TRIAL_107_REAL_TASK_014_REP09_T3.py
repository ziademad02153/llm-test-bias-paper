def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]

def test_custom_factor_and_base():
    """Test with custom factor and base values."""
    result = compute_exponential_backoff_sequence(4, base=3.0, factor=0.5)
    assert result == [0.5, 1.5, 4.5, 13.5]

def test_max_value_bound():
    """Test sequence is bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, max_value=10.0)
    assert result == [1.0, 2.0, 4.0, 8.0, 10.0]

def test_zero_attempts():
    """Test edge case with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_max_value_none():
    """Test behavior when max_value is None (no bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    assert result == [1.0, 2.0, 4.0]

def test_all_custom_parameters():
    """Test with all custom parameters provided."""
    result = compute_exponential_backoff_sequence(3, base=1.5, factor=2.0, max_value=5.0)
    assert result == [2.0, 3.0, 4.5]