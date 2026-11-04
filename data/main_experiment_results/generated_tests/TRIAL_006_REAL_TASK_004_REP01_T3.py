def test_empty_tags_string():
    valid, msg = validate_tags("", {"python", "api"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    valid, msg = validate_tags("python|api|coding|test", {"python", "api", "coding", "test"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag():
    valid, msg = validate_tags("python|invalid", {"python", "api"})
    assert not valid
    assert "not in valid_tag_set" in msg

def test_valid_tags():
    valid, msg = validate_tags("python|api", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tag_in_middle():
    valid, msg = validate_tags("python||api", {"python", "api"})
    assert not valid
    assert "non-empty tags" in msg

def test_single_valid_tag():
    valid, msg = validate_tags("python", {"python", "api"})
    assert valid
    assert msg == ""