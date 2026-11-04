def test_standard_case():
    """Test standard case with multiple fields."""
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    """Test empty positions list returns entire line stripped."""
    line = "  hello world  "
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["hello world"]

def test_single_position():
    """Test single position splits into two fields."""
    line = "foo bar baz"
    positions = [4]
    result = split_by_positions(line, positions)
    assert result == ["foo", "bar baz"]

def test_positions_beyond_length():
    """Test positions beyond line length return empty strings."""
    line = "short"
    positions = [5, 10]
    result = split_by_positions(line, positions)
    assert result == ["", ""]

def test_empty_line():
    """Test empty line returns empty fields."""
    line = ""
    positions = [0, 2, 4]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_whitespace_fields():
    """Test fields with only whitespace are stripped to empty strings."""
    line = "a   b    c  "
    positions = [0, 2, 5, 8]
    result = split_by_positions(line, positions)
    assert result == ["a", "", "b", "c"]