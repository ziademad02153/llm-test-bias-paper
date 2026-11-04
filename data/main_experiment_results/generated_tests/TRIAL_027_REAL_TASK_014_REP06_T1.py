import unittest

class TestComputeExponentialBackoffSequence(unittest.TestCase):
    def test_standard_input(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        expected_result = [1.0, 2.0, 4.0, 8.0, 16.0]
        self.assertEqual(result, expected_result)

    def test_empty_attempts(self):
        attempts = 0
        base = 2.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(result, [])

    def test_max_value_bound(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        expected_result = [1.0, 2.0, 4.0, 8.0]
        self.assertEqual(result, expected_result)

    def test_max_value_none(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = None
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        expected_result = [1.0, 2.0, 4.0, 8.0, 16.0]
        self.assertEqual(result, expected_result)

    def test_factor_zero(self):
        attempts = 5
        base = 2.0
        factor = 0.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()