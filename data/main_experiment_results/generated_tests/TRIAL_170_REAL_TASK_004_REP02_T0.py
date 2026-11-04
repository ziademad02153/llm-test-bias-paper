import unittest
from typing import Tuple, Set
from your_module import validate_tags  # Assuming the function is in your_module

class TestValidateTags(unittest.TestCase):

    def test_valid_tags(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | python | api"
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], "")  # error_message should be empty

    def test_empty_string(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = ""
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], "Input string is empty")  # error_message should be "Input string is empty"

    def test_single_tag(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding"
        result = validate_tags(tags, valid_tag_set)
        self.assertTrue(result[0])  # is_valid should be True
        self.assertEqual(result[1], "")  # error_message should be empty

    def test_four_tags(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | python | api | other"
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], "Too many tags (4)")  # error_message should be "Too many tags (4)"

    def test_invalid_tag(self):
        valid_tag_set = {"coding", "python", "api"}
        tags = "coding | invalid | api"
        result = validate_tags(tags, valid_tag_set)
        self.assertFalse(result[0])  # is_valid should be False
        self.assertEqual(result[1], "Invalid tag: invalid")  # error_message should be "Invalid tag: invalid"

if __name__ == "__main__":
    unittest.main()
```

This test suite covers various scenarios, including:

*   A valid input with multiple tags
*   An empty input string
*   A single tag
*   An input with too many tags (four in this case)
*   An input with an invalid tag

Each test case includes an assertion to verify the expected behavior of the `validate_tags` function. The `unittest.main()` call at the end runs the test suite.