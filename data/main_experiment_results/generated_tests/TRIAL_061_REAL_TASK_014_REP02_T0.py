import unittest
from typing import List, Union

def compute_exponential_backoff_sequence(attempts: int, base: float = 2.0, factor: float = 1.0, max_value: float | None = None) -> List[float]:
    # implementation omitted

def test_compute_exponential_backoff_sequence_standard_inputs():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]

def test_compute_exponential_backoff_sequence_empty_inputs():
    attempts = 0
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == 0

def test_compute_exponential_backoff_sequence_bounds():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 8.0]

def test_compute_exponential_backoff_sequence_max_value():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = 10.0
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 8.0]

def test_compute_exponential_backoff_sequence_max_value_none():
    attempts = 5
    base = 2.0
    factor = 1.0
    max_value = None
    result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
    assert len(result) == attempts
    assert result == [1.0, 2.0, 4.0, 8.0, 16.0]

def test_compute_exponential_backoff_sequence_negative_attempts():
    attempts = -1
    base = 2.0
    factor = 1.0
    max_value = None
    with unittest.assertRaises(ValueError):
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)

def test_compute_exponential_backoff_sequence_negative_base():
    attempts = 5
    base = -2.0
    factor = 1.0
    max_value = None
    with unittest.assertRaises(ValueError):
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)

def test_compute_exponential_backoff_sequence_negative_factor():
    attempts = 5
    base = 2.0
    factor = -1.0
    max_value = None
    with unittest.assertRaises(ValueError):
        compute_exponential_backoff_sequence(attempts, base, factor, max_value)