def test_empty_string():
    """Test that empty string returns False with appropriate error message."""
    valid, msg = validate_tags("", {"python", "api", "coding"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    """Test that more than 3 tags returns False with appropriate error message."""
    valid, msg = validate_tags("python|api|coding|dev", {"python", "api", "coding", "dev"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag():
    """Test that invalid tag returns False with appropriate error message."""
    valid, msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not valid
    assert "not in valid tag set" in msg

def test_valid_tags():
    """Test that valid tags return True and empty error message."""
    valid, msg = validate_tags("python|api", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tag_in_middle():
    """Test that empty tag in the middle (e.g., 'a||b') is invalid."""
    valid, msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not valid
    assert "non-empty tags" in msg

def test_single_valid_tag():
    """Test that a single valid tag is accepted."""
    valid, msg = validate_tags("python", {"python", "api", "coding"})
    assert valid
    assert msg == ""