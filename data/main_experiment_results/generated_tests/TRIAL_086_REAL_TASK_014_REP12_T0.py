import unittest
from your_module import compute_exponential_backoff_sequence

class TestComputeExponentialBackoffSequence(unittest.TestCase):

    def test_standard_input(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertAlmostEqual(result[0], factor * (base ** 1))
        self.assertAlmostEqual(result[1], factor * (base ** 2))
        self.assertAlmostEqual(result[2], factor * (base ** 3))
        self.assertAlmostEqual(result[3], factor * (base ** 4))
        self.assertAlmostEqual(result[4], factor * (base ** 5))

    def test_empty_inputs(self):
        attempts = 0
        base = 2.0
        factor = 1.0
        max_value = 100.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), 0)

    def test_bounds(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = 1.0
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertAlmostEqual(result[0], factor * (base ** 1))
        self.assertAlmostEqual(result[1], factor * (base ** 2))
        self.assertAlmostEqual(result[2], factor * (base ** 3))
        self.assertAlmostEqual(result[3], factor * (base ** 4))
        self.assertAlmostEqual(result[4], max_value)

    def test_max_value_none(self):
        attempts = 5
        base = 2.0
        factor = 1.0
        max_value = None
        result = compute_exponential_backoff_sequence(attempts, base, factor, max_value)
        self.assertEqual(len(result), attempts)
        self.assertAlmostEqual(result[0], factor * (base ** 1))
        self.assertAlmostEqual(result[1], factor * (base ** 2))
        self.assertAlmostEqual(result[2], factor * (base ** 3))
        self.assertAlmostEqual(result[3], factor * (base ** 4))
        self.assertAlmostEqual(result[4], factor * (base ** 5))

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the following scenarios:

*   `test_standard_input`: Verifies the function's behavior with standard inputs.
*   `test_empty_inputs`: Tests the function's behavior when the input `attempts` is 0.
*   `test_bounds`: Tests the function's behavior when the `max_value` is reached.
*   `test_max_value_none`: Tests the function's behavior when `max_value` is `None`.

Each test function uses `assertAlmostEqual` to compare the actual and expected values, considering floating-point precision issues. The `unittest.main()` call at the end runs the test suite.