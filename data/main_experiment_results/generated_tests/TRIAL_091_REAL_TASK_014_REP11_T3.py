# Test standard inputs
def test_standard_inputs():
    assert compute_exponential_backoff_sequence(3) == [2.0, 4.0, 8.0]
    assert compute_exponential_backoff_sequence(3, base=3.0, factor=0.5) == [1.5, 4.5, 13.5]
    assert compute_exponential_backoff_sequence(2, factor=2.0, max_value=10.0) == [4.0, 8.0]

# Test edge case with zero attempts
def test_zero_attempts():
    assert compute_exponential_backoff_sequence(0) == []

# Test edge case with max_value bounding
def test_max_value_bounding():
    assert compute_exponential_backoff_sequence(5, max_value=10.0) == [2.0, 4.0, 8.0, 10.0, 10.0]

# Test edge case with factor zero
def test_factor_zero():
    assert compute_exponential_backoff_sequence(3, factor=0.0) == [0.0, 0.0, 0.0]

# Test edge case with base one
def test_base_one():
    assert compute_exponential_backoff_sequence(3, base=1.0) == [1.0, 1.0, 1.0]

# Test edge case with max_value zero
def test_max_value_zero():
    assert compute_exponential_backoff_sequence(3, max_value=0.0) == [0.0, 0.0, 0.0]