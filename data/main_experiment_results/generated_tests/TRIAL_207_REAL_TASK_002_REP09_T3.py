def test_standard_case():
    """Test standard case with multiple fields."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_line():
    """Test empty input line."""
    line = ""
    positions = [0, 2, 4]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_single_field():
    """Test case with only one field covering the entire line."""
    line = "  foo bar  "
    positions = [0]
    result = split_by_positions(line, positions)
    assert result == ["foo bar"]

def test_positions_beyond_line_length():
    """Test case where positions exceed line length."""
    line = "abc"
    positions = [0, 2, 4, 6]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c", "", ""]

def test_whitespace_fields():
    """Test case with fields containing only whitespace."""
    line = "  a   b     "
    positions = [0, 3, 6, 9]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", ""]

def test_empty_positions():
    """Test case with empty positions list (should return empty list)."""
    line = "abc def"
    positions = []
    result = split_by_positions(line, positions)
    assert result == []