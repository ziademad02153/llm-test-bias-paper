def test_empty_tags_string():
    """Test that an empty tags string is invalid."""
    valid, msg = validate_tags("", {"python", "coding", "api"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    """Test that more than 3 tags is invalid."""
    valid, msg = validate_tags("python|coding|api|web", {"python", "coding", "api", "web"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag():
    """Test that a tag not in valid_tag_set is invalid."""
    valid, msg = validate_tags("python|rust", {"python", "coding", "api"})
    assert not valid
    assert "not in valid_tag_set" in msg

def test_valid_tags():
    """Test that a valid tags string passes validation."""
    valid, msg = validate_tags("python|coding", {"python", "coding", "api"})
    assert valid
    assert msg == ""

def test_empty_tag_in_middle():
    """Test that empty tags within the string are invalid."""
    valid, msg = validate_tags("python||api", {"python", "coding", "api"})
    assert not valid
    assert "non-empty tags" in msg

def test_single_valid_tag():
    """Test that a single valid tag passes validation."""
    valid, msg = validate_tags("python", {"python", "coding", "api"})
    assert valid
    assert msg == ""