def test_compute_exponential_backoff_sequence_standard_inputs():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    expected = [1.0, 2.0, 4.0, 8.0, 16.0]
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected


def test_compute_exponential_backoff_sequence_empty_inputs():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    expected = []
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected


def test_compute_exponential_backoff_sequence_max_value_bound():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 16.0
    expected = [1.0, 2.0, 4.0, 8.0, 16.0]
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected


def test_compute_exponential_backoff_sequence_max_value_not_bound():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 32.0
    expected = [1.0, 2.0, 4.0, 8.0, 16.0]
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected


def test_compute_exponential_backoff_sequence_factor_not_1():
    attempts = 5
    base = 2.0
    factor = 2.0
    max_value = None
    expected = [2.0, 4.0, 8.0, 16.0, 32.0]
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected


def test_compute_exponential_backoff_sequence_base_not_2():
    attempts = 5
    base = 3.0
    factor = 1.0
    max_value = None
    expected = [1.0, 3.0, 9.0, 27.0, 81.0]
    assert compute_exponential_backoff_sequence(attempts, base, factor, max_value) == expected