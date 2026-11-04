def test_compute_fibonacci_backoff_sequence_zero_attempts():
    assert compute_fibonacci_backoff_sequence(0) == []

def test_compute_fibonacci_backoff_sequence_one_attempt():
    assert compute_fibonacci_backoff_sequence(1) == [0.0]

def test_compute_fibonacci_backoff_sequence_five_attempts():
    assert compute_fibonacci_backoff_sequence(5) == [0.0, 1.0, 1.0, 2.0, 3.0]

def test_compute_fibonacci_backoff_sequence_with_max_value():
    assert compute_fibonacci_backoff_sequence(5, max_value=1.5) == [0.0, 1.0, 1.0, 1.5, 1.5]

def test_compute_fibonacci_backoff_sequence_large_attempts():
    assert compute_fibonacci_backoff_sequence(10) == [0.0, 1.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21, 34.0]

def test_compute_fibonacci_backoff_sequence_max_value_less_than_first_delay():
    assert compute_fibonacci_backoff_sequence(3, max_value=0.5) == [0.0, 0.5, 0.5]