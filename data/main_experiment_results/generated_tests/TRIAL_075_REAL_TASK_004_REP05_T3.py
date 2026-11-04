Here's a comprehensive suite of unit tests for the `validate_tags` function based on its specification:

```python
# Test 1: Valid input with 1 tag
def test_valid_single_tag():
    valid_tags = {'python', 'coding', 'api'}
    result, msg = validate_tags('python', valid_tags)
    assert result is True
    assert msg == ''

# Test 2: Valid input with 3 tags
def test_valid_three_tags():
    valid_tags = {'python', 'coding', 'api', 'test'}
    result, msg = validate_tags('python | coding | api', valid_tags)
    assert result is True
    assert msg == ''

# Test 3: Empty input string
def test_empty_input():
    valid_tags = {'python', 'coding'}
    result, msg = validate_tags('', valid_tags)
    assert result is False
    assert 'Non-empty string required' in msg

# Test 4: Too many tags (4 tags)
def test_too_many_tags():
    valid_tags = {'a', 'b', 'c', 'd', 'e'}
    result, msg = validate_tags('a | b | c | d', valid_tags)
    assert result is False
    assert 'at most 3 non-empty tags' in msg

# Test 5: Invalid tag not in valid set
def test_invalid_tag():
    valid_tags = {'valid', 'tags'}
    result, msg = validate_tags('valid | invalid', valid_tags)
    assert result is False
    assert 'not in valid tag set' in msg

# Test 6: Empty tag in the middle
def test_empty_middle_tag():
    valid_tags = {'a', 'b', 'c'}
    result, msg = validate_tags('a || c', valid_tags)
    assert result is False
    assert 'non-empty tags' in msg