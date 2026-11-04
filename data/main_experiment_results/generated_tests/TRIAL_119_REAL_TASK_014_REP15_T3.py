def test_standard_sequence():
    """Test standard exponential backoff sequence without max_value."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=1.0)
    assert result == [1.0, 2.0, 4.0], f"Expected [1.0, 2.0, 4.0], got {result}"

def test_with_factor():
    """Test sequence with a custom factor."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=0.5)
    assert result == [0.5, 1.0, 2.0], f"Expected [0.5, 1.0, 2.0], got {result}"

def test_with_max_value():
    """Test sequence bounded by max_value."""
    result = compute_exponential_backoff_sequence(5, base=2.0, factor=1.0, max_value=3.0)
    assert result == [1.0, 2.0, 3.0, 3.0, 3.0], f"Expected [1.0, 2.0, 3.0, 3.0, 3.0], got {result}"

def test_zero_attempts():
    """Test edge case with zero attempts (empty sequence)."""
    result = compute_exponential_backoff_sequence(0, base=2.0, factor=1.0)
    assert result == [], f"Expected [], got {result}"

def test_non_default_base():
    """Test sequence with a non-default base value."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=1.0)
    assert result == [1.0, 3.0, 9.0], f"Expected [1.0, 3.0, 9.0], got {result}"

def test_max_value_equals_first_term():
    """Test when max_value equals the first term in the sequence."""
    result = compute_exponential_backoff_sequence(3, base=2.0, factor=1.0, max_value=1.0)
    assert result == [1.0, 1.0, 1.0], f"Expected [1.0, 1.0, 1.0], got {result}"