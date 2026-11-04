def test_empty_string_invalid():
    """Test that empty string is invalid."""
    valid, msg = validate_tags("", {"python", "api"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags_invalid():
    """Test that more than 3 tags is invalid."""
    valid, msg = validate_tags("python|api|web|testing", {"python", "api", "web", "testing"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag_invalid():
    """Test that unrecognized tags are invalid."""
    valid, msg = validate_tags("python|rust", {"python", "api"})
    assert not valid
    assert "not in valid_tag_set" in msg

def test_valid_tags_return_true():
    """Test that valid tags return True."""
    valid, msg = validate_tags("python|api", {"python", "api", "web"})
    assert valid
    assert msg == ""

def test_empty_tags_invalid():
    """Test that empty tags (e.g., '||') are invalid."""
    valid, msg = validate_tags("python||api", {"python", "api"})
    assert not valid
    assert "non-empty tags" in msg

def test_single_valid_tag_returns_true():
    """Test that a single valid tag is accepted."""
    valid, msg = validate_tags("python", {"python", "api"})
    assert valid
    assert msg == ""