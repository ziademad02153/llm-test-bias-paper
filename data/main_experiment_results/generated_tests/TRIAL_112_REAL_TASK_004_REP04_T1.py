def test_empty_string():
    assert validate_tags("", {"coding", "python", "api"}) == (False, "Input string is empty")

def test_zero_tags():
    assert validate_tags(" | ", {"coding", "python", "api"}) == (False, "Number of tags is not between 1 and 3")

def test_four_tags():
    assert validate_tags("coding | python | api | testing", {"coding", "python", "api"}) == (False, "Number of tags is not between 1 and 3")

def test_invalid_tag():
    assert validate_tags("coding | invalid_tag | api", {"coding", "python", "api"}) == (False, "One or more tags are not in the valid tag set")

def test_valid_tags():
    assert validate_tags("coding | python | api", {"coding", "python", "api"}) == (True, "")

def test_valid_tag_set():
    assert validate_tags("coding | python | api", {"coding", "python", "api", "testing"}) == (True, "")

def test_single_tag():
    assert validate_tags("coding", {"coding", "python", "api"}) == (True, "")

def test_three_tags():
    assert validate_tags("coding | python | api", {"coding", "python", "api"}) == (True, "")