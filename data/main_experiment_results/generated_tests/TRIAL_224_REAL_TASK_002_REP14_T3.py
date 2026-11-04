def test_standard_case():
    """Test normal case with multiple fields."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    """Test empty positions list returns entire line stripped."""
    line = "  foo bar  "
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["foo bar"]

def test_positions_beyond_line_length():
    """Test positions beyond line length are handled gracefully."""
    line = "abc"
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["ab", "c"]

def test_empty_line():
    """Test empty line returns empty strings for each field."""
    line = ""
    positions = [0, 1, 3]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_whitespace_fields():
    """Test fields containing only whitespace are stripped to empty."""
    line = "a    b  c  "
    positions = [0, 2, 5, 7]
    result = split_by_positions(line, positions)
    assert result == ["a", "", "b", "c"]

def test_single_position():
    """Test single position splits into two fields."""
    line = "foo bar"
    positions = [3]
    result = split_by_positions(line, positions)
    assert result == ["foo", "bar"]