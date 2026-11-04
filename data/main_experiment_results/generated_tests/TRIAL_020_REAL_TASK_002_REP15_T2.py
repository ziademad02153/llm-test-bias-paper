def test_basic_split():
    line = "abc def ghi jkl"
    positions = [4, 8, 12]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi", "jkl"]

def test_empty_line():
    line = ""
    positions = [2, 4, 6]
    assert split_by_positions(line, positions) == []

def test_positions_beyond_line_length():
    line = "short"
    positions = [10, 20]
    assert split_by_positions(line, positions) == ["short"]

def test_whitespace_stripping():
    line = "  a  b  c  d  "
    positions = [3, 6, 9]
    assert split_by_positions(line, positions) == ["a", "b", "c", "d"]

def test_empty_positions():
    line = "some text"
    positions = []
    assert split_by_positions(line, positions) == ["some text"]

def test_adjacent_positions():
    line = "abcdef"
    positions = [2, 2, 4, 4]
    assert split_by_positions(line, positions) == ["ab", "cd", "ef"]