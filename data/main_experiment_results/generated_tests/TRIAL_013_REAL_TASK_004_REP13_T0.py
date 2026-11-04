import unittest
from typing import Tuple, Set
from your_module import validate_tags  # Assuming the function is in a module named 'your_module'

class TestValidateTags(unittest.TestCase):

    def test_valid_tags(self):
        # Test valid tags with 1, 2, and 3 tags
        valid_tags = ['coding', 'python', 'api']
        valid_tag_set = {'coding', 'python', 'api'}
        result = validate_tags('|'.join(valid_tags), valid_tag_set)
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_empty_string(self):
        # Test empty string
        tags = ''
        valid_tag_set = {'coding', 'python', 'api'}
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Input string cannot be empty.')  # error_message should be 'Input string cannot be empty.'

    def test_too_few_tags(self):
        # Test too few tags (less than 1)
        tags = '|'
        valid_tag_set = {'coding', 'python', 'api'}
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'At least 1 tag is required.')  # error_message should be 'At least 1 tag is required.'

    def test_too_many_tags(self):
        # Test too many tags (more than 3)
        tags = '|'.join(['coding', 'python', 'api', 'java', 'c++'])
        valid_tag_set = {'coding', 'python', 'api'}
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'At most 3 tags are allowed.')  # error_message should be 'At most 3 tags are allowed.'

    def test_invalid_tag(self):
        # Test invalid tag
        tags = '|'.join(['coding', 'python', 'api', 'invalid_tag'])
        valid_tag_set = {'coding', 'python', 'api'}
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Invalid tag: invalid_tag')  # error_message should be 'Invalid tag: invalid_tag'

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the following cases:

1.  **Valid tags**: Test with 1, 2, and 3 valid tags.
2.  **Empty string**: Test an empty input string.
3.  **Too few tags**: Test with fewer than 1 tag.
4.  **Too many tags**: Test with more than 3 tags.
5.  **Invalid tag**: Test with an invalid tag.

Each test case checks the `is_valid` and `error_message` returned by the `validate_tags` function.