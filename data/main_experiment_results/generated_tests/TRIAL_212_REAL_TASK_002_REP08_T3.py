def test_basic_split():
    """Test basic splitting with multiple positions."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    """Test with empty positions list (should return whole line stripped)."""
    line = "  foo bar  "
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["foo bar"]

def test_single_position():
    """Test with single position (should split into two parts)."""
    line = "abc def"
    positions = [3]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def"]

def test_positions_beyond_length():
    """Test with positions beyond line length (should handle gracefully)."""
    line = "abc"
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c", ""]

def test_empty_line():
    """Test with empty line (should return empty strings for each field)."""
    line = ""
    positions = [0, 1, 2]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_whitespace_fields():
    """Test fields that are entirely whitespace (should be stripped to empty)."""
    line = "a   b  c  "
    positions = [0, 1, 2, 5, 7]
    result = split_by_positions(line, positions)
    assert result == ["a", "", "", "b", "c"]