def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]  # factor=1.0, base=2.0: 1*(2^0), 1*(2^1), 1*(2^2)
    assert result == expected

def test_custom_factor_and_base():
    """Test with custom factor and base."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    expected = [0.5, 1.5, 4.5]  # 0.5*(3^0), 0.5*(3^1), 0.5*(3^2)
    assert result == expected

def test_max_value_bound():
    """Test sequence is capped by max_value."""
    result = compute_exponential_backoff_sequence(5, base=2.0, factor=1.0, max_value=3.0)
    expected = [1.0, 2.0, 3.0, 3.0, 3.0]  # 1*(2^0), 1*(2^1), 3.0 (cap), 3.0, 3.0
    assert result == expected

def test_zero_attempts():
    """Test edge case with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_no_max_value():
    """Test sequence grows without bound when max_value is None."""
    result = compute_exponential_backoff_sequence(4, base=10.0, factor=1.0, max_value=None)
    expected = [1.0, 10.0, 100.0, 1000.0]  # 1*(10^0), 1*(10^1), etc.
    assert result == expected

def test_negative_attempts_raises_error():
    """Test negative attempts raises ValueError (implied by spec)."""
    try:
        compute_exponential_backoff_sequence(-1)
        assert False, "Expected ValueError for negative attempts"
    except ValueError:
        pass