import unittest

class TestComputeExponentialBackoffSequence(unittest.TestCase):

    def test_standard_input(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], factor * (base ** 0))
        self.assertEqual(result[1], factor * (base ** 1))
        self.assertEqual(result[2], factor * (base ** 2))
        self.assertEqual(result[3], factor * (base ** 3))
        self.assertEqual(result[4], factor * (base ** 4))

    def test_empty_inputs(self):
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
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], factor * (base ** 0))
        self.assertEqual(result[1], factor * (base ** 1))
        self.assertEqual(result[2], factor * (base ** 2))
        self.assertEqual(result[3], factor * (base ** 3))
        self.assertEqual(result[4], factor * (base ** 4))

    def test_max_value_none(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = None
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertEqual(result[0], factor * (base ** 0))
        self.assertEqual(result[1], factor * (base ** 1))
        self.assertEqual(result[2], factor * (base ** 2))
        self.assertEqual(result[3], factor * (base ** 3))
        self.assertEqual(result[4], factor * (base ** 4))

    def test_factor_zero(self):
        attempts = 5
        base = 2.0
        factor = 0.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(result, [])

    def test_base_zero(self):
        attempts = 5
        base = 0.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()