import unittest
from typing import Tuple, Set
from your_module import validate_tags  # Assuming the function is in a module named 'your_module'

class TestValidateTags(unittest.TestCase):

    def test_valid_tags(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = 'coding | python | api'
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_empty_string(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = ''
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Input string is empty')  # error_message should be 'Input string is empty'

    def test_single_tag(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = 'coding'
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], '')  # error_message should be empty

    def test_four_tags(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = 'coding | python | api | testing'
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Input string contains more than 3 tags')  # error_message should be 'Input string contains more than 3 tags'

    def test_invalid_tag(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = 'invalid | coding | python'
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Invalid tag: invalid')  # error_message should be 'Invalid tag: invalid'

    def test_no_tags(self):
        valid_tag_set = {'coding', 'python', 'api'}
        tags = '   |   |   '
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], 'Input string is empty')  # error_message should be 'Input string is empty'

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the following scenarios:

1.  Valid input with multiple tags.
2.  Empty input string.
3.  Single tag input.
4.  Input with more than 3 tags.
5.  Input with an invalid tag.
6.  Input with leading/trailing whitespace.

Each test case checks the `is_valid` and `error_message` returned by the `validate_tags` function.