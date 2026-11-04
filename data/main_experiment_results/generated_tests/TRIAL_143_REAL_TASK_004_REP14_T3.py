def test_empty_tags_string():
    """Test that empty tags string returns False with appropriate error message."""
    valid, msg = validate_tags("", {"python", "api", "coding"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    """Test that more than 3 tags returns False with appropriate error message."""
    valid, msg = validate_tags("python|api|coding|test", {"python", "api", "coding", "test"})
    assert not valid
    assert "Must contain at least 1 and at most 3 non-empty tags" in msg

def test_invalid_tag():
    """Test that invalid tags return False with appropriate error message."""
    valid, msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not valid
    assert "not in valid tag set" in msg

def test_valid_tags():
    """Test that valid tags return True with empty error message."""
    valid, msg = validate_tags("python|api", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tags_after_split():
    """Test that empty tags after splitting return False with appropriate error message."""
    valid, msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not valid
    assert "Must contain at least 1 and at most 3 non-empty tags" in msg

def test_single_valid_tag():
    """Test that a single valid tag returns True with empty error message."""
    valid, msg = validate_tags("python", {"python", "api", "coding"})
    assert valid
    assert msg == ""