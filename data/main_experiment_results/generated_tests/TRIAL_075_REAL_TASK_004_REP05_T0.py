def test_valid_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api', valid_tag_set) == (True, '')

def test_empty_string():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('', valid_tag_set) == (False, 'Input string is empty')

def test_single_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding', valid_tag_set) == (True, '')

def test_four_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api | invalid', valid_tag_set) == (False, 'Input string contains more than 3 tags')

def test_invalid_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | invalid', valid_tag_set) == (False, 'Tag "invalid" is not in the allowed set')

def test_valid_tag_set_empty():
    valid_tag_set = set()
    assert validate_tags('coding | python | api', valid_tag_set) == (False, 'Input string contains invalid tags')

def test_valid_tag_set_single_element():
    valid_tag_set = {'coding'}
    assert validate_tags('coding', valid_tag_set) == (True, '')
```

This suite of tests covers the following scenarios:

- A valid input string with multiple tags.
- An empty input string.
- A single tag.
- An input string with more than 3 tags.
- An input string with an invalid tag.
- A valid tag set that is empty.
- A valid tag set with a single element.

Each test case checks the function's behavior against the specified rules.