def test_valid_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api', valid_tag_set) == (True, '')

def test_invalid_tags_count():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python', valid_tag_set) == (False, 'Expected 1 to 3 tags, got 2')

def test_invalid_tags_empty():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('', valid_tag_set) == (False, 'Non-empty string required')

def test_invalid_tags_empty_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags(' | python | api', valid_tag_set) == (False, 'Invalid tag: ')

def test_invalid_tags_out_of_bounds():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | python | api | another', valid_tag_set) == (False, 'Expected 1 to 3 tags, got 4')

def test_invalid_tags_not_in_set():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | invalid | api', valid_tag_set) == (False, 'Invalid tag: invalid')

def test_empty_valid_tag_set():
    valid_tag_set = set()
    assert validate_tags('coding | python | api', valid_tag_set) == (False, 'Every tag must be present in valid_tag_set')
```

This suite of tests covers the following cases:

1. Valid tags string with 3 tags.
2. Invalid tags count (too few or too many tags).
3. Empty input string.
4. Empty tag in the input string.
5. Tags count out of bounds (more than 3 tags).
6. Invalid tag not present in the valid tag set.
7. Empty valid tag set.

Each test case uses the `assert` statement to verify the expected behavior of the `validate_tags` function. If the function behaves as expected, the test will pass; otherwise, it will fail and provide an error message.