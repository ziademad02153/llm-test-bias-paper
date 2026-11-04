def test_basic_splitting():
    line = "abc def  ghi  "
    positions = [4, 8]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi"]

def test_empty_line():
    line = ""
    positions = [2, 4]
    assert split_by_positions(line, positions) == []

def test_positions_beyond_line_length():
    line = "abc"
    positions = [5, 10]
    assert split_by_positions(line, positions) == ["abc"]

def test_empty_positions():
    line = "abc def"
    positions = []
    assert split_by_positions(line, positions) == ["abc def"]

def test_whitespace_only_fields():
    line = "a  b   c"
    positions = [2, 5]
    assert split_by_positions(line, positions) == ["a", "b", "c"]

def test_adjacent_positions():
    line = "abcdef"
    positions = [2, 2, 4, 4]
    assert split_by_positions(line, positions) == ["ab", "cd", "ef"]