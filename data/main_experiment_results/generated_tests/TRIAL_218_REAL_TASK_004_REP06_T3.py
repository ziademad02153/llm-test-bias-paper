def test_empty_string():
    """Test that an empty string is rejected."""
    valid, msg = validate_tags("", {"python", "api", "coding"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    """Test that more than 3 tags are rejected."""
    valid, msg = validate_tags("python|api|coding|web", {"python", "api", "coding", "web"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag():
    """Test that invalid tags are rejected."""
    valid, msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not valid
    assert "not in valid_tag_set" in msg

def test_valid_tags():
    """Test that valid tags are accepted."""
    valid, msg = validate_tags("python|api", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tags_in_middle():
    """Test that empty tags (e.g., due to extra pipes) are rejected."""
    valid, msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not valid
    assert "non-empty tags" in msg

def test_single_valid_tag():
    """Test that a single valid tag is accepted."""
    valid, msg = validate_tags("python", {"python", "api", "coding"})
    assert valid
    assert msg == ""