from typing import List

def split_by_positions(line: str, positions: List[int]) -> List[str]:
    fields = []
    prev_pos = 0
    for pos in positions:
        field = line[prev_pos:pos].strip()
        if field:
            fields.append(field)
        prev_pos = pos
    last_field = line[prev_pos:].strip()
    if last_field:
        fields.append(last_field)
    return fields

def test_standard_input():
    assert split_by_positions("hello world", [6]) == ["hello", "world"]

def test_empty_input():
    assert split_by_positions("", []) == []

def test_empty_fields():
    assert split_by_positions("   hello   world   ", [3, 9]) == ["hello", "world"]

def test_out_of_bounds():
    assert split_by_positions("hello", [10]) == ["hello"]

def test_consecutive_positions():
    assert split_by_positions("hello world", [0, 6, 11]) == ["", "hello", "world"]

def test_single_position():
    assert split_by_positions("hello world", [5]) == ["hello", "world"]

# Test edge case with negative position
try:
    split_by_positions("hello world", [-1])
    assert False, "Expected ValueError for negative position"
except ValueError:
    pass

# Test edge case with non-integer position
try:
    split_by_positions("hello world", [1.5])
    assert False, "Expected TypeError for non-integer position"
except TypeError:
    pass