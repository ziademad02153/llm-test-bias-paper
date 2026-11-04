def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]  # factor=1.0, base=2.0: 1*(2**0), 1*(2**1), 1*(2**2)
    assert result == expected

def test_custom_factor_and_base():
    """Test with custom factor and base values."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    expected = [0.5, 1.5, 4.5]  # 0.5*(3**0), 0.5*(3**1), 0.5*(3**2)
    assert result == expected

def test_max_value_bound():
    """Test sequence is capped by max_value."""
    result = compute_exponential_backoff_sequence(5, base=2.0, factor=1.0, max_value=3.0)
    expected = [1.0, 2.0, 3.0, 3.0, 3.0]  # Values beyond 3.0 are capped
    assert result == expected

def test_zero_attempts():
    """Test edge case with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_negative_attempts():
    """Test edge case with negative attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(-1)
    assert result == []

def test_max_value_none():
    """Test max_value=None (no upper bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    expected = [1.0, 2.0, 4.0]  # No capping
    assert result == expected