# Test the compute_exponential_backoff_sequence function
def test_standard_input():
    assert compute_exponential_backoff_sequence(5) == [1.0, 2.0, 4.0, 8.0, 16.0]

def test_factor_and_base():
    assert compute_exponential_backoff_sequence(5, base=3.0, factor=2.0) == [6.0, 24.0, 96.0, 384.0, 1536.0]

def test_max_value():
    assert compute_exponential_backoff_sequence(5, max_value=10.0) == [1.0, 2.0, 4.0, 8.0, 10.0]

def test_max_value_with_factor():
    assert compute_exponential_backoff_sequence(5, factor=2.0, max_value=20.0) == [4.0, 8.0, 16.0, 32.0, 64.0]

def test_empty_attempts():
    assert compute_exponential_backoff_sequence(0) == []

def test_max_value_none():
    assert compute_exponential_backoff_sequence(5, max_value=None) == [1.0, 2.0, 4.0, 8.0, 16.0]