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
    assert validate_tags('coding | python | api | invalid', valid_tag_set) == (False, 'Input string contains 4 tags, expected 1-3')

def test_invalid_tag():
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags('coding | invalid | api', valid_tag_set) == (False, 'Invalid tag: invalid')

def test_empty_valid_tag_set():
    valid_tag_set = set()
    assert validate_tags('coding | python | api', valid_tag_set) == (False, 'No valid tags provided')