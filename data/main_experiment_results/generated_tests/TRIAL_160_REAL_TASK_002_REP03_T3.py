def test_standard_input():
    line = "abc def  ghi  "
    positions = [0, 4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_line():
    line = ""
    positions = [0, 2, 5]
    result = split_by_positions(line, positions)
    assert result == ["", "", ""]

def test_positions_beyond_line_length():
    line = "short"
    positions = [0, 3, 10]
    result = split_by_positions(line, positions)
    assert result == ["sho", "rt", ""]

def test_whitespace_stripping():
    line = "  a  b   c  "
    positions = [0, 3, 6]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c"]

def test_single_position():
    line = "abcdef"
    positions = [0]
    result = split_by_positions(line, positions)
    assert result == ["abcdef"]

def test_adjacent_positions():
    line = "abc123xyz"
    positions = [0, 3, 6]
    result = split_by_positions(line, positions)
    assert result == ["abc", "123", "xyz"]