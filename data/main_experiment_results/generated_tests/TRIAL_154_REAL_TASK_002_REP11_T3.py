def test_standard_case():
    """Test splitting a line with multiple fields."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_line():
    """Test splitting an empty line."""
    line = ""
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_single_field():
    """Test splitting a line into a single field."""
    line = "  hello  "
    positions = [0]
    result = split_by_positions(line, positions)
    assert result == ["hello"]

def test_positions_beyond_line_length():
    """Test positions that extend beyond the line length."""
    line = "abc"
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c", ""]

def test_whitespace_fields():
    """Test fields that are entirely whitespace."""
    line = "a    b  c  "
    positions = [0, 2, 5, 7]
    result = split_by_positions(line, positions)
    assert result == ["a", "", "b", "c"]

def test_no_positions():
    """Test empty positions list (should return entire line as single field)."""
    line = "foo bar"
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["foo bar"]