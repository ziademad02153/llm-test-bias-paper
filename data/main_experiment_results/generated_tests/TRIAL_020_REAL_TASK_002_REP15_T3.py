def test_standard_case():
    """Test standard case with multiple fields."""
    line = "abc  def   ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]


def test_empty_positions():
    """Test with empty positions list (should return entire line stripped)."""
    line = "  hello world  "
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["hello world"]


def test_single_position():
    """Test with single position (should split into two fields)."""
    line = "foo bar baz"
    positions = [4]
    result = split_by_positions(line, positions)
    assert result == ["foo", "bar baz"]


def test_positions_beyond_line_length():
    """Test with positions beyond line length (last field should be empty)."""
    line = "short"
    positions = [0, 3, 10]
    result = split_by_positions(line, positions)
    assert result == ["sho", "rt", ""]


def test_empty_line():
    """Test with empty line (should return empty strings for each field)."""
    line = ""
    positions = [0, 2, 4]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]


def test_adjacent_positions():
    """Test with adjacent positions (zero-width fields)."""
    line = "a b c"
    positions = [0, 1, 1, 3, 3]
    result = split_by_positions(line, positions)
    assert result == ["a", "", " b", "", " c"]