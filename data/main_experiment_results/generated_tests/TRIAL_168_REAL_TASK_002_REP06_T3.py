def test_basic_splitting():
    """Test basic splitting with multiple positions."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    """Test with empty positions list (should return entire line stripped)."""
    line = "  foo bar  "
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["foo bar"]

def test_single_position():
    """Test with a single position (should split into two parts)."""
    line = "abc def"
    positions = [3]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def"]

def test_positions_beyond_line_length():
    """Test with positions beyond line length (last field should be empty)."""
    line = "abc"
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c", ""]

def test_whitespace_fields():
    """Test fields that are entirely whitespace (should be stripped to empty)."""
    line = "a   b    c  "
    positions = [0, 2, 5, 8]
    result = split_by_positions(line, positions)
    assert result == ["a", "", "b", "c"]

def test_empty_line():
    """Test with an empty input line."""
    line = ""
    positions = [0, 1, 2]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]