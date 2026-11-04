def test_basic_sequence():
    """Test basic sequence with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0]

def test_with_custom_factor():
    """Test sequence with a custom factor."""
    result = compute_exponential_backoff_sequence(3, factor=0.5)
    assert result == [0.5, 1.0, 2.0]

def test_with_max_value():
    """Test sequence with max_value constraint."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    assert result == [1.0, 2.0, 4.0]

def test_zero_attempts():
    """Test edge case with zero attempts."""
    result = compute_exponential_backoff_sequence(0)
    assert result == []

def test_non_default_base():
    """Test sequence with a non-default base."""
    result = compute_exponential_backoff_sequence(3, base=3.0)
    assert result == [1.0, 3.0, 9.0]

def test_max_value_exact_boundary():
    """Test sequence where max_value equals a term in the sequence."""
    result = compute_exponential_backoff_sequence(4, max_value=4.0)
    assert result == [1.0, 2.0, 4.0]