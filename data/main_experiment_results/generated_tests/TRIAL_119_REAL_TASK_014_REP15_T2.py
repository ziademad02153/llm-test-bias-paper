def test_standard_input():
    """Test standard inputs with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    expected = [1.0, 2.0, 4.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_custom_base_and_factor():
    """Test with custom base and factor."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    expected = [0.5, 1.5, 4.5]
    assert result == expected, f"Expected {expected}, got {result}"

def test_max_value_bound():
    """Test max_value bounds the sequence."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    expected = [1.0, 2.0, 4.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_zero_attempts():
    """Test zero attempts returns empty list."""
    result = compute_exponential_backoff_sequence(0)
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

def test_max_value_none():
    """Test max_value=None does not bound the sequence."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    expected = [1.0, 2.0, 4.0]
    assert result == expected, f"Expected {expected}, got {result}"

def test_all_values_exceed_max_value():
    """Test when all values exceed max_value, returns empty list."""
    result = compute_exponential_backoff_sequence(3, max_value=0.5)
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"