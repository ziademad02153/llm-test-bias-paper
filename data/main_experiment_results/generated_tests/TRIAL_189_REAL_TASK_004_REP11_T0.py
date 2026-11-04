def test_valid_tags():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (True, "")

def test_empty_string():
    tags = ""
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (False, "Input string is empty")

def test_too_few_tags():
    tags = "coding"
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (False, "Must contain at least 1 and at most 3 non-empty tags")

def test_too_many_tags():
    tags = "coding | python | api | testing"
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (False, "Must contain at least 1 and at most 3 non-empty tags")

def test_invalid_tag():
    tags = "coding | invalid | api"
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (False, "Every tag must be present in valid_tag_set")

def test_valid_tag():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api"}
    assert validate_tags(tags, valid_tag_set) == (True, "")

def test_valid_tag_set_empty():
    tags = "coding | python | api"
    valid_tag_set = set()
    assert validate_tags(tags, valid_tag_set) == (False, "Every tag must be present in valid_tag_set")

def test_valid_tag_set_single_element():
    tags = "coding | python | api"
    valid_tag_set = {"coding"}
    assert validate_tags(tags, valid_tag_set) == (False, "Every tag must be present in valid_tag_set")