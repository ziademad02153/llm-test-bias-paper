def test_empty_string():
    """Test that an empty string is invalid."""
    valid, msg = validate_tags("", {"python", "api", "coding"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    """Test that more than 3 tags is invalid."""
    valid, msg = validate_tags("python|api|coding|dev", {"python", "api", "coding", "dev"})
    assert not valid
    assert "Must contain at least 1 and at most 3 non-empty tags" in msg

def test_invalid_tag():
    """Test that a tag not in valid_tag_set is invalid."""
    valid, msg = validate_tags("python|rust", {"python", "api", "coding"})
    assert not valid
    assert "not in valid tag set" in msg.lower()

def test_valid_tags():
    """Test a valid pipe-separated tag string."""
    valid, msg = validate_tags("python|coding", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tag_in_middle():
    """Test that empty tags (e.g., '||') are invalid."""
    valid, msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not valid
    assert "non-empty tags" in msg.lower()

def test_single_valid_tag():
    """Test that a single valid tag passes."""
    valid, msg = validate_tags("python", {"python", "api", "coding"})
    assert valid
    assert msg == ""