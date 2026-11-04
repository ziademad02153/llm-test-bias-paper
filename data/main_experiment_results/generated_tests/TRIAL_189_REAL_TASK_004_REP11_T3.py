def test_empty_string():
    """Test empty input string."""
    is_valid, error_msg = validate_tags("", {"python", "api", "coding"})
    assert not is_valid
    assert "Non-empty string required" in error_msg

def test_too_many_tags():
    """Test more than 3 tags."""
    is_valid, error_msg = validate_tags("python|api|coding|testing", {"python", "api", "coding", "testing"})
    assert not is_valid
    assert "Must contain at least 1 and at most 3 non-empty tags" in error_msg

def test_invalid_tag():
    """Test unrecognized tag."""
    is_valid, error_msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not is_valid
    assert "not in valid tag set" in error_msg.lower()

def test_valid_tags():
    """Test valid input with 2 tags."""
    is_valid, error_msg = validate_tags("python|coding", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""

def test_empty_tag_in_middle():
    """Test empty tag in the middle (e.g., 'python||coding')."""
    is_valid, error_msg = validate_tags("python||coding", {"python", "api", "coding"})
    assert not is_valid
    assert "non-empty tags" in error_msg.lower()

def test_single_valid_tag():
    """Test single valid tag."""
    is_valid, error_msg = validate_tags("python", {"python", "api", "coding"})
    assert is_valid
    assert error_msg == ""