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
    assert split_by_positions("Hello World", [6]) == ["Hello", "World"]

def test_empty_input():
    assert split_by_positions("", []) == []

def test_empty_positions():
    assert split_by_positions("Hello World", []) == ["Hello World"]

def test_empty_line():
    assert split_by_positions("", [1, 2]) == []

def test_positions_out_of_bounds():
    assert split_by_positions("Hello", [10]) == ["Hello"]

def test_consecutive_positions():
    assert split_by_positions("Hello World", [0, 0, 6]) == ["", "Hello", "World"]

def test_positions_with_whitespace():
    assert split_by_positions("   Hello   World   ", [3, 9]) == ["Hello", "World"]

def test_last_field_empty():
    assert split_by_positions("Hello World  ", [6, 11]) == ["Hello", "World"]

def test_all_fields_empty():
    assert split_by_positions("   ", [0, 1, 2]) == ["", "", ""]

def test_field_with_only_whitespace():
    assert split_by_positions("Hello   World", [6]) == ["Hello", "World"]