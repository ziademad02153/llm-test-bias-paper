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

def test_empty_line():
    assert split_by_positions("", [1, 2]) == []

def test_no_positions():
    assert split_by_positions("hello world", []) == ["hello world"]

def test_positions_out_of_bounds():
    assert split_by_positions("hello", [10]) == ["hello"]

def test_consecutive_positions():
    assert split_by_positions("hello world", [0, 6, 11]) == ["", "hello", "world"]

def test_positions_at_start_and_end():
    assert split_by_positions("hello world", [0, 11]) == ["", "hello world"]

def test_empty_fields():
    assert split_by_positions("   hello   world   ", [3, 9, 15]) == ["hello", "world"]

def test_single_position():
    assert split_by_positions("hello world", [6]) == ["hello", "world"]

def test_multiple_positions():
    assert split_by_positions("hello world this is a test", [6, 12, 16, 20]) == ["hello", "world", "this", "is a test"]

def test_position_at_end():
    assert split_by_positions("hello world", [11]) == ["hello world"]

def test_position_at_start():
    assert split_by_positions("hello world", [0]) == ["", "hello world"]

def test_position_in_middle():
    assert split_by_positions("hello world", [6]) == ["hello", "world"]

def test_position_out_of_range():
    assert split_by_positions("hello", [100]) == ["hello"]

def test_negative_position():
    try:
        split_by_positions("hello", [-1])
        assert False, "Expected ValueError for negative position"
    except ValueError:
        assert True

def test_non_integer_position():
    try:
        split_by_positions("hello", [1.5])
        assert False, "Expected TypeError for non-integer position"
    except TypeError:
        assert True

def test_position_list_not_sorted():
    try:
        split_by_positions("hello", [5, 1])
        assert False, "Expected ValueError for unsorted position list"
    except ValueError:
        assert True

def test_position_list_with_duplicates():
    try:
        split_by_positions("hello", [1, 1])
        assert False, "Expected ValueError for position list with duplicates"
    except ValueError:
        assert True