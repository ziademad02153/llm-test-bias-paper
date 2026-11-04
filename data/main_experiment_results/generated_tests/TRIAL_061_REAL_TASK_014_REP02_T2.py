def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]

def test_with_custom_factor_and_base():
    """Test with custom factor and base."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    assert result == [0.5, 1.5, 4.5]

def test_with_max_value():
    """Test with max_value limiting the sequence."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    assert result == [1.0, 2.0, 4.0]

def test_zero_attempts():
    """Test with zero attempts (edge case)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_max_value_exact_boundary():
    """Test when max_value equals one of the sequence values."""
    result = compute_exponential_backoff_sequence(4, max_value=4.0)
    assert result == [1.0, 2.0, 4.0]

def test_all_values_exceed_max_value():
    """Test when all generated values exceed max_value."""
    result = compute_exponential_backoff_sequence(3, max_value=0.5)
    assert result == []