def test_empty_string():
    is_valid, error_msg = validate_tags("", {"python", "api", "coding"})
    assert not is_valid
    assert "Non-empty string required" in error_msg

def test_too_many_tags():
    is_valid, error_msg = validate_tags("python|api|coding|test", {"python", "api", "coding", "test"})
    assert not is_valid
    assert "at most 3 non-empty tags" in error_msg

def test_invalid_tag():
    is_valid, error_msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not is_valid
    assert "not in valid tag set" in error_msg

def test_valid_tags():
    is_valid, error_msg = validate_tags("python|api", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""

def test_empty_tag_in_middle():
    is_valid, error_msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not is_valid
    assert "empty tag" in error_msg

def test_single_valid_tag():
    is_valid, error_msg = validate_tags("python", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""