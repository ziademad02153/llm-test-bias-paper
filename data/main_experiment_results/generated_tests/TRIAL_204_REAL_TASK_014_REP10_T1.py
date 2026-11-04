import unittest

class TestComputeExponentialBackoffSequence(unittest.TestCase):

    def test_standard_inputs(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], factor)
        self.assertEqual(result[-1], max_value)

    def test_empty_inputs(self):
        attempts = 0
        base = 2.0
        factor = 1.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), 0)

    def test_bounds(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertLessEqual(result[-1], max_value)

    def test_max_value_none(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = None
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)

    def test_factor_zero(self):
        attempts = 5
        base = 2.0
        factor = 0.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], 0.0)

    def test_base_one(self):
        attempts = 5
        base = 1.0
        factor = 1.0
        max_value = 10.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], 1.0)

if __name__ == '__main__':
    unittest.main()