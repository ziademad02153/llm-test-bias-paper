def test_valid_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = 'coding | python | api'
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, '')

def test_empty_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = ''
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, 'Invalid input: empty string')

def test_single_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = 'coding'
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, '')

def test_four_tags():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = 'coding | python | api | testing'
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, 'Invalid input: more than 3 tags')

def test_invalid_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = 'coding | invalid | api'
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, 'Invalid input: invalid tag "invalid"')

def test_empty_valid_tag_set():
    valid_tag_set = set()
    tags = 'coding | python | api'
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, 'Invalid input: empty valid tag set')

def test_non_empty_valid_tag_set():
    valid_tag_set = {'coding', 'python', 'api'}
    tags = ''
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, 'Invalid input: empty string')