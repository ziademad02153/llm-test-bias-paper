def test_zero_attempts():
    assert compute_fibonacci_backoff_sequence(0) == def test_one_attempt():
    assert compute_fibonacci_backoff_sequence(1) == [1.0]

def test_five_attempts():
    assert compute_fibonacci_backoff_sequence(5) == [1.0, 1.0, 2.0, 3.0, 5.0]

def test_max_value_less_than_first_fibonacci():
    assert compute_fibonacci_backoff_sequence(3, max_value=0.5) == def test_max_value_equal_to_first_fibonacci():
    assert compute_fibonacci_backoff_sequence(3, max_value=1.0) == [1.0, 1.0]

def test_max_value_between_fibonacci_numbers():
    assert compute_fibonacci_backoff_sequence(5, max_value=3.5) == [1.0, 1.0, 2.0, 3.0]