def test_basic_splitting():
    line = "abc def  ghi  "
    positions = [4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    line = "abc def"
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["abc def"]

def test_empty_line():
    line = ""
    positions = [2, 4]
    result = split_by_positions(line, positions)
    assert result == []

def test_whitespace_only_fields():
    line = "a   b  c  "
    positions = [2, 5, 7]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c"]

def test_positions_beyond_line_length():
    line = "abc"
    positions = [5, 10]
    result = split_by_positions(line, positions)
    assert result == ["abc"]

def test_adjacent_positions():
    line = "a b c"
    positions = [1, 2, 3, 4]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c"]