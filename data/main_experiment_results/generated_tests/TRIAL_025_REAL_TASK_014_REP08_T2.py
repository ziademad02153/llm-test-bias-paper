def test_standard_inputs():
    """Test standard inputs with default parameters."""
    result = compute_exponential_backoff_sequence(3)
    assert result == [1.0, 2.0, 4.0], f"Expected [1.0, 2.0, 4.0], got {result}"

def test_custom_base_and_factor():
    """Test custom base and factor values."""
    result = compute_exponential_backoff_sequence(3, base=3.0, factor=0.5)
    assert result == [0.5, 1.5, 4.5], f"Expected [0.5, 1.5, 4.5], got {result}"

def test_max_value_bound():
    """Test max_value bounds the sequence."""
    result = compute_exponential_backoff_sequence(5, max_value=5.0)
    assert result == [1.0, 2.0, 4.0], f"Expected [1.0, 2.0, 4.0], got {result}"

def test_zero_attempts():
    """Test zero attempts returns empty list."""
    result = compute_exponential_backoff_sequence(0)
    assert result == [], f"Expected [], got {result}"

def test_max_value_none():
    """Test max_value=None does not bound the sequence."""
    result = compute_exponential_backoff_sequence(3, max_value=None)
    assert result == [1.0, 2.0, 4.0], f"Expected [1.0, 2.0, 4.0], got {result}"

def test_all_values_exceed_max_value():
    """Test all values exceed max_value, resulting in empty list."""
    result = compute_exponential_backoff_sequence(3, max_value=0.5)
    assert result == [], f"Expected [], got {result}"