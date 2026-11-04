def test_valid_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api', valid_tag_set) == (True, '')

def test_empty_string():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('', valid_tag_set) == (False, 'Input string is empty')

def test_single_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding', valid_tag_set) == (True, '')

def test_multiple_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api | invalid', valid_tag_set) == (False, 'More than 3 tags are not allowed')

def test_invalid_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | invalid', valid_tag_set) == (False, 'Invalid tag: invalid')

def test_too_few_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding', valid_tag_set) == (False, 'At least 1 tag is required')

def test_too_many_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api | invalid | another', valid_tag_set) == (False, 'More than 3 tags are not allowed')
```

This suite of tests covers the following scenarios:

- Valid input with multiple tags
- Empty input string
- Single tag input
- Input with more than 3 tags
- Input with an invalid tag
- Input with less than 1 tag

Each test case checks the function's behavior against the specified rules. The `assert` statements are used to verify the expected output of the function.