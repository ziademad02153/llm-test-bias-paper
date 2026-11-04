def test_valid_tags():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_empty_string():
    tags = ""
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Input string is empty")

def test_single_tag():
    tags = "coding"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_four_tags():
    tags = "coding | python | api | invalid"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Invalid tag 'invalid'")

def test_five_tags():
    tags = "coding | python | api | invalid | another"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Invalid tag 'invalid'")

def test_valid_tag_set_empty():
    tags = "coding | python | api"
    valid_tag_set = set()
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Invalid tag 'coding'")

def test_valid_tag_set_single_element():
    tags = "coding"
    valid_tag_set = {"coding"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_valid_tag_set_multiple_elements():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api", "another"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_valid_tag_set_multiple_elements_with_invalid_tag():
    tags = "coding | python | api | invalid"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Invalid tag 'invalid'")