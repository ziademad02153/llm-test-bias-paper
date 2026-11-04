def test_basic_splitting():
    line = "abc def  ghi  "
    positions = [4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    line = "hello world"
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["hello world"]

def test_empty_line():
    line = ""
    positions = [2, 5]
    result = split_by_positions(line, positions)
    assert result == []

def test_positions_beyond_line_length():
    line = "short"
    positions = [3, 10, 15]
    result = split_by_positions(line, positions)
    assert result == ["sho", "rt"]

def test_whitespace_only_fields():
    line = "a  b   c   "
    positions = [2, 5, 8]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c"]

def test_adjacent_positions():
    line = "abcdef"
    positions = [2, 2, 4, 4]
    result = split_by_positions(line, positions)
    assert result == ["ab", "cd", "ef"]