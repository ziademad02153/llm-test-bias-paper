def test_basic_splitting():
    line = "abc def ghi jkl"
    positions = [4, 8, 12]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi", "jkl"]

def test_empty_line():
    line = ""
    positions = [2, 5, 8]
    assert split_by_positions(line, positions) == []

def test_whitespace_handling():
    line = "  abc  def  ghi  jkl  "
    positions = [6, 12, 18]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi", "jkl"]

def test_empty_fields_skipped():
    line = "abc   def   ghi   jkl"
    positions = [4, 8, 12]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi", "jkl"]

def test_positions_beyond_line_length():
    line = "abc def"
    positions = [4, 20, 30]
    assert split_by_positions(line, positions) == ["abc", "def"]

def test_no_positions():
    line = "abc def ghi"
    positions = []
    assert split_by_positions(line, positions) == ["abc def ghi"]