def test_standard_input():
    assert compute_fibonacci_backoff_sequence(5) == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_max_value():
    assert compute_fibonacci_backoff_sequence(10, max_value=8.0) == [1.0, 1.0, 2.0, 3.0, 5.0, 8.0]

def test_zero_attempts():
    assert compute_fibonacci_backoff_sequence(0) == []

def test_negative_attempts():
    assert compute_fibonacci_backoff_sequence(-5) == []

def test_max_value_zero():
    assert compute_fibonacci_backoff_sequence(5, max_value=0.0) == []

def test_max_value_negative():
    assert compute_fibonacci_backoff_sequence(5, max_value=-1.0) == []