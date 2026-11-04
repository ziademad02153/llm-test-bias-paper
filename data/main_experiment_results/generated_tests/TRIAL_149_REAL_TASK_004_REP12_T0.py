import unittest
from typing import Tuple, Set
from your_module import validate_tags  # Assuming the function is in a module named 'your_module'

class TestValidateTags(unittest.TestCase):

    def test_valid_tags(self):
        # Test valid tags with exactly 1 tag
        result = validate_tags('coding', {'coding', 'python', 'api'})
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_valid_tags_multiple(self):
        # Test valid tags with exactly 2 tags
        result = validate_tags('coding | python', {'coding', 'python', 'api'})
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_valid_tags_max(self):
        # Test valid tags with exactly 3 tags
        result = validate_tags('coding | python | api', {'coding', 'python', 'api'})
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_empty_string(self):
        # Test empty string
        result = validate_tags('', {'coding', 'python', 'api'})
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Non-empty string required.')  # error_message should be 'Non-empty string required.'

    def test_invalid_tag(self):
        # Test invalid tag
        result = validate_tags('coding | invalid_tag', {'coding', 'python', 'api'})
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Invalid tag: invalid_tag.')  # error_message should be 'Invalid tag: invalid_tag.'

    def test_invalid_tag_multiple(self):
        # Test multiple invalid tags
        result = validate_tags('coding | invalid_tag | invalid_tag', {'coding', 'python', 'api'})
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Invalid tag: invalid_tag.')  # error_message should be 'Invalid tag: invalid_tag.'

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the following cases:

*   Valid tags with exactly 1 tag
*   Valid tags with exactly 2 tags
*   Valid tags with exactly 3 tags
*   Empty string
*   Invalid tag
*   Multiple invalid tags

Each test case checks the `is_valid` and `error_message` returned by the `validate_tags` function. The `unittest.main()` call at the end runs all the test cases.