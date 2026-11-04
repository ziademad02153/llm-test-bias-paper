# Test 1: Valid input with exactly 3 tags
def test_valid_input_with_3_tags():
    tags = 'coding | python | api'
    valid_tag_set = {'coding', 'python', 'api', 'devops'}
    assert validate_tags(tags, valid_tag_set) == (True, "")

# Test 2: Empty input string
def test_empty_input_string():
    tags = ''
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags(tags, valid_tag_set) == (False, "Non-empty string required.")

# Test 3: Input with more than 3 tags
def test_input_with_more_than_3_tags():
    tags = 'coding | python | api | devops'
    valid_tag_set = {'coding', 'python', 'api', 'devops'}
    assert validate_tags(tags, valid_tag_set) == (False, "Must contain at least 1 and at most 3 non-empty tags.")

# Test 4: Input with invalid tag
def test_input_with_invalid_tag():
    tags = 'coding | java | api'
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags(tags, valid_tag_set) == (False, "Every tag must be present in valid_tag_set.")

# Test 5: Input with exactly 1 tag
def test_input_with_exactly_1_tag():
    tags = 'coding'
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags(tags, valid_tag_set) == (True, "")

# Test 6: Input with empty tags (e.g., 'coding || api')
def test_input_with_empty_tags():
    tags = 'coding || api'
    valid_tag_set = {'coding', 'python', 'api'}
    assert validate_tags(tags, valid_tag_set) == (False, "Must contain at least 1 and at most 3 non-empty tags.")