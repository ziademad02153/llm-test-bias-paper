import unittest

class TestComputeExponentialBackoffSequence(unittest.TestCase):

    def test_standard_inputs(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 10.0
        expected = [1.0, 2.0, 4.0, 8.0, 9.0]
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

    def test_empty_inputs(self):
        attempts = 0
        base = 2.0
        factor = 1.0
        max_value = 10.0
        expected = []
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

    def test_max_value_bound(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 10.0
        expected = [1.0, 2.0, 4.0, 8.0, 9.0]
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

    def test_max_value_exceeded(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 5.0
        expected = [1.0, 2.0, 4.0, 8.0, 16.0]
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

    def test_factor_zero(self):
        attempts = 5
        base = 2.0
        factor = 0.0
        max_value = 10.0
        expected = []
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

    def test_base_zero(self):
        attempts = 5
        base = 0.0
        factor = 1.0
        max_value = 10.0
        expected = []
        self.assertEqual(compute_exponential_backoff_sequence(attempts, base, factor, max_value), expected)

if __name__ == "__main__":
    unittest.main()