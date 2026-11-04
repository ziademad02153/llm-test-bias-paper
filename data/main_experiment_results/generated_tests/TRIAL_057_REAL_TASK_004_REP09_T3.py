def test_empty_string():
    """Test empty input string."""
    is_valid, error_msg = validate_tags("", {"python", "api"})
    assert not is_valid
    assert "Non-empty string required" in error_msg

def test_too_many_tags():
    """Test more than 3 tags."""
    is_valid, error_msg = validate_tags("python|api|coding|test", {"python", "api", "coding", "test"})
    assert not is_valid
    assert "at most 3 non-empty tags" in error_msg

def test_invalid_tag():
    """Test with a tag not in valid_tag_set."""
    is_valid, error_msg = validate_tags("python|invalid", {"python", "api"})
    assert not is_valid
    assert "not in valid_tag_set" in error_msg

def test_valid_tags():
    """Test valid input with 2 tags."""
    is_valid, error_msg = validate_tags("python|api", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""

def test_min_max_tags():
    """Test bounds (1 and 3 tags)."""
    # Test 1 tag
    is_valid, error_msg = validate_tags("python", {"python", "api"})
    assert is_valid
    assert error_msg == ""

    # Test 3 tags
    is_valid, error_msg = validate_tags("python|api|coding", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""

def test_empty_tags_in_string():
    """Test empty tags within the string (e.g., 'python||api')."""
    is_valid, error_msg = validate_tags("python||api", {"python", "api"})
    assert not is_valid
    assert "non-empty tags" in error_msg