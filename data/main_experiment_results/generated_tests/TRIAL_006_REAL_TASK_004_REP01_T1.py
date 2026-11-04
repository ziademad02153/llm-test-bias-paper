import unittest
from typing import Tuple, Set
from your_module import validate_tags  # Replace 'your_module' with the actual module name

class TestValidateTags(unittest.TestCase):

    def test_valid_tags(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | python | api"
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])
        self.assertEqual(result[1], "")

    def test_empty_input(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = ""
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])
        self.assertEqual(result[1], "Input string is empty")

    def test_single_tag(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding"
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])
        self.assertEqual(result[1], "")

    def test_multiple_tags(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | python"
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])
        self.assertEqual(result[1], "")

    def test_too_many_tags(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | python | api | invalid"
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])
        self.assertEqual(result[1], "Number of tags is not between 1 and 3")

    def test_invalid_tag(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | invalid"
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])
        self.assertEqual(result[1], "One or more tags are not in the valid tag set")

if __name__ == "__main__":
    unittest.main()
```

This test suite covers the following scenarios:

1.  Valid tags: Tests the function with a valid pipe-separated string of tags.
2.  Empty input: Verifies that the function returns `False` and an error message when given an empty input string.
3.  Single tag: Checks that the function returns `True` and an empty error message when given a single tag.
4.  Multiple tags: Tests the function with a pipe-separated string of multiple valid tags.
5.  Too many tags: Verifies that the function returns `False` and an error message when given a string with more than three tags.
6.  Invalid tag: Checks that the function returns `False` and an error message when given a string with an invalid tag.