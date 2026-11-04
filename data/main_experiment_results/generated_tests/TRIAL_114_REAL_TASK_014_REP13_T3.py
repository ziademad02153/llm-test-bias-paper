def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]

def test_custom_factor_and_base():
    """Test with custom factor and base values."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    assert result == [0.5, 1.5, 4.5]

def test_max_value_bound():
    """Test sequence is bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    assert result == [1.0, 2.0, 4.0, 5.0, 5.0]

def test_zero_attempts():
    """Test edge case with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_max_value_none():
    """Test behavior when max_value is None (no bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    assert result == [1.0, 2.0, 4.0]

def test_large_attempts():
    """Test large number of attempts with max_value."""
    result = compute_exponential_backoff_sequence(10, max_value=100.0)
    assert len(result) == 10
    assert all(x <= 100.0 for x in result)