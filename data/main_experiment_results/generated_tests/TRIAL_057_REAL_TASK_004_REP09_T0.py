def test_valid_tags():
    assert validate_tags('coding | python | api', {'coding', 'python', 'api'}) == (True, '')

def test_empty_string():
    assert validate_tags('', {'coding', 'python', 'api'}) == (False, 'Input string cannot be empty')

def test_single_tag():
    assert validate_tags('coding', {'coding', 'python', 'api'}) == (True, '')

def test_multiple_tags():
    assert validate_tags('coding | python | api | testing', {'coding', 'python', 'api', 'testing'}) == (True, '')

def test_too_many_tags():
    assert validate_tags('coding | python | api | testing | devops', {'coding', 'python', 'api', 'testing'}) == (False, 'Too many tags (max 3 allowed)')

def test_invalid_tag():
    assert validate_tags('coding | invalid-tag', {'coding', 'python', 'api'}) == (False, 'Invalid tag: invalid-tag')

def test_valid_tag_set_empty():
    assert validate_tags('coding | python | api', set()) == (False, 'Invalid tag: coding')

def test_valid_tag_set_single_element():
    assert validate_tags('coding', {'coding'}) == (True, '')

def test_valid_tag_set_multiple_elements():
    assert validate_tags('coding | python | api', {'coding', 'python', 'api'}) == (True, '')

def test_valid_tag_set_too_many_elements():
    assert validate_tags('coding | python | api | testing', {'coding', 'python', 'api', 'testing', 'devops'}) == (True, '')

def test_valid_tag_set_invalid_element():
    assert validate_tags('coding | invalid-tag', {'coding', 'python', 'api'}) == (False, 'Invalid tag: invalid-tag')