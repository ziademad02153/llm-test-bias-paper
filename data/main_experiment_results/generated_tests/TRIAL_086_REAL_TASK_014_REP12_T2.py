def test_standard_case():
    """Test standard case with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2
    assert result == expected

def test_with_custom_factor():
    """Test with a custom factor."""
    result = compute_exponential_backoff_sequence(3, factor=0.5)
    expected = [0.5, 1.0, 2.0]  # 0.5 * 2^0, 0.5 * 2^1, 0.5 * 2^2
    assert result == expected

def test_with_max_value():
    """Test with a max_value constraint."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2 (2^3=8 > 5, so excluded)
    assert result == expected

def test_zero_attempts():
    """Test with zero attempts (edge case)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_non_default_base():
    """Test with a non-default base."""
    result = compute_exponential_backoff_sequence(3, base=3.0)
    expected = [1.0, 3.0, 9.0]  # 3^0, 3^1, 3^2
    assert result == expected

def test_max_value_equals_single_element():
    """Test when max_value equals a single element in the sequence."""
    result = compute_exponential_backoff_sequence(3, max_value=2.0)
    expected = [1.0, 2.0]  # 2^0, 2^1 (2^2=4 > 2, so excluded)
    assert result == expected