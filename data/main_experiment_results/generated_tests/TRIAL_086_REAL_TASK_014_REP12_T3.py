def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]  # factor=1.0, base=2.0: 1*(2**0), 1*(2**1), 1*(2**2)

def test_custom_factor_and_base():
    """Test with custom factor and base."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    assert result == [0.5, 1.5, 4.5]  # 0.5*(3**0), 0.5*(3**1), 0.5*(3**2)

def test_max_value_bound():
    """Test sequence bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, base=2.0, factor=1.0, max_value=5.0)
    assert result == [1.0, 2.0, 4.0, 5.0, 5.0]  # Last two values capped at 5.0

def test_zero_attempts():
    """Test edge case with zero attempts."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_negative_attempts_raises_error():
    """Test negative attempts raises ValueError."""
    try:
        compute_exponential_backoff_sequence(-1)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        pass

def test_max_value_none():
    """Test max_value=None (no bound)."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    assert result == [1.0, 2.0, 4.0]