def test_basic_sequence():
    """Test basic exponential backoff sequence with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2
    assert result == expected

def test_with_custom_factor():
    """Test sequence with a custom factor."""
    result = compute_exponential_backoff_sequence(3, factor=0.5)
    expected = [0.5, 1.0, 2.0]  # 0.5 * 2^0, 0.5 * 2^1, 0.5 * 2^2
    assert result == expected

def test_with_max_value():
    """Test sequence with a max_value constraint."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2 (2^3=8 > 5, so excluded)
    assert result == expected

def test_zero_attempts():
    """Test edge case with zero attempts (empty list)."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_non_default_base():
    """Test sequence with a non-default base."""
    result = compute_exponential_backoff_sequence(3, base=3.0)
    expected = [1.0, 3.0, 9.0]  # 3^0, 3^1, 3^2
    assert result == expected

def test_max_value_equals_some_element():
    """Test when max_value equals one of the sequence elements."""
    result = compute_exponential_backoff_sequence(4, max_value=4.0)
    expected = [1.0, 2.0, 4.0]  # 2^0, 2^1, 2^2 (2^3=8 > 4, so excluded)
    assert result == expected