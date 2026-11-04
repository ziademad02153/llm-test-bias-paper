def test_compute_exponential_backoff_sequence_empty_attempts():
    assert compute_exponential_backoff_sequence(0) == []

def test_compute_exponential_backoff_sequence_single_attempt():
    assert compute_exponential_backoff_sequence(1) == [1.0]

def test_compute_exponential_backoff_sequence_multiple_attempts():
    assert compute_exponential_backoff_sequence(3) == [1.0, 2.0, 4.0]

def test_compute_exponential_backoff_sequence_with_factor():
    assert compute_exponential_backoff_sequence(3, factor=2.0) == [2.0, 4.0, 8.0]

def test_compute_exponential_backoff_sequence_with_base():
    assert compute_exponential_backoff_sequence(3, base=3.0) == [3.0, 9.0, 27.0]

def test_compute_exponential_backoff_sequence_with_max_value():
    assert compute_exponential_backoff_sequence(3, max_value=10.0) == [1.0, 2.0, 4.0]

def test_compute_exponential_backoff_sequence_with_max_value_and_factor():
    assert compute_exponential_backoff_sequence(3, max_value=10.0, factor=2.0) == [2.0, 4.0, 8.0]

def test_compute_exponential_backoff_sequence_with_max_value_and_base():
    assert compute_exponential_backoff_sequence(3, max_value=10.0, base=3.0) == [3.0, 9.0, 27.0]

def test_compute_exponential_backoff_sequence_with_max_value_and_factor_and_base():
    assert compute_exponential_backoff_sequence(3, max_value=10.0, factor=2.0, base=3.0) == [6.0, 18.0, 54.0]