def test_standard_case():
    line = "abc def  ghi  jkl"
    positions = [0, 4, 8, 12]
    assert split_by_positions(line, positions) == ["abc", "def", "ghi", "jkl"]

def test_empty_line():
    line = ""
    positions = [0, 2, 4]
    assert split_by_positions(line, positions) == ["", "", ""]

def test_positions_beyond_line_length():
    line = "short"
    positions = [0, 3, 10]
    assert split_by_positions(line, positions) == ["sho", "rt"]

def test_whitespace_stripping():
    line = "  a  b c   d  "
    positions = [0, 3, 5, 7]
    assert split_by_positions(line, positions) == ["a", "b", "c", "d"]

def test_single_position():
    line = "complete"
    positions = [0]
    assert split_by_positions(line, positions) == ["complete"]

def test_empty_positions():
    line = "any line"
    positions = []
    assert split_by_positions(line, positions) == []