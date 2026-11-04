def test_standard_case():
    """Test standard exponential backoff sequence."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=1.0)
    assert result == [1.0, 2.0, 4.0]

def test_with_factor():
    """Test sequence with custom factor."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=0.5)
    assert result == [0.5, 1.0, 2.0]

def test_with_max_value():
    """Test sequence bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, base=2.0, factor=1.0, max_value=5.0)
    assert result == [1.0, 2.0, 4.0, 5.0, 5.0]

def test_zero_attempts():
    """Test with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_non_default_base():
    """Test with non-default base value."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=1.0)
    assert result == [1.0, 3.0, 9.0]

def test_max_value_none():
    """Test with max_value=None (no upper bound)."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=1.0, max_value=None)
    assert result == [1.0, 2.0, 4.0]