Here's a comprehensive set of unit tests for the `split_by_positions` function:

```python
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

def test_positions_beyond_line_length():
    line = "abc"
    positions = [5, 10]
    result = split_by_positions(line, positions)
    assert result == ["abc"]

def test_empty_line():
    line = ""
    positions = [2, 4]
    result = split_by_positions(line, positions)
    assert result == []

def test_whitespace_only_fields():
    line = "a   b  c"
    positions = [2, 5]
    result = split_by_positions(line, positions)
    assert result == ["a", "b", "c"]

def test_adjacent_positions():
    line = "abcdef"
    positions = [2, 2, 4, 4]
    result = split_by_positions(line, positions)
    assert result == ["ab", "cd", "ef"]
```

This test suite covers:
1. Basic functionality with normal input
2. Empty positions list (should return entire line as one field)
3. Positions beyond the line length (should return remaining content)
4. Empty input line (should return empty list)
5. Whitespace handling (should strip and skip empty fields)
6. Adjacent/duplicate positions (should handle zero-width fields correctly)

All tests use simple assert statements and are independent of any testing framework.