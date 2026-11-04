def test_basic_split():
    line = "abc def ghi"
    positions = [4, 8]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_line():
    line = ""
    positions = [2, 5]
    result = split_by_positions(line, positions)
    assert result == []

def test_positions_beyond_line_length():
    line = "abc"
    positions = [5, 10]
    result = split_by_positions(line, positions)
    assert result == ["abc"]

def test_whitespace_stripping():
    line = "  abc  def  ghi  "
    positions = [7, 12]
    result = split_by_positions(line, positions)
    assert result == ["abc", "def", "ghi"]

def test_empty_positions():
    line = "abc def"
    positions = []
    result = split_by_positions(line, positions)
    assert result == ["abc def"]

def test_adjacent_positions():
    line = "abcdef"
    positions = [2, 2, 4, 4]
    result = split_by_positions(line, positions)
    assert result == ["ab", "cd", "ef"]