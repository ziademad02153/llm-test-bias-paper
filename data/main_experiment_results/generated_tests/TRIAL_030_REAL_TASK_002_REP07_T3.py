def test_standard_case():
    """Test standard case with multiple fields."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_line():
    """Test empty input line."""
    line = ""
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["", ""]

def test_single_field():
    """Test case with single field spanning entire line."""
    line = "  hello world  "
    positions = [0]
    result = split_by_positions(line, positions)
    assert result == ["hello world"]

def test_positions_beyond_line_length():
    """Test positions extending beyond line length."""
    line = "abc"
    positions = [0, 2, 5, 10]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c", ""]

def test_whitespace_fields():
    """Test fields containing only whitespace."""
    line = "  a   b     c  "
    positions = [0, 3, 7, 12]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c", ""]

def test_empty_positions():
    """Test empty positions list (should return entire line as single field)."""
    line = "abc def"
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["abc def"]