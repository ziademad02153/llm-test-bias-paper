def test_standard_case():
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

def test_single_field():
    line = "  hello world  "
    positions = [0]
    result = split_by_positions(line, positions)
    assert result == ["hello world"]

def test_whitespace_fields():
    line = "a  b   c    "
    positions = [0, 2, 5, 8]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c", ""]

def test_adjacent_positions():
    line = "abcdef"
    positions = [0, 3, 3, 6]
    result = split_by_positions(line, positions)
    assert result == ["abc", "", "def"]