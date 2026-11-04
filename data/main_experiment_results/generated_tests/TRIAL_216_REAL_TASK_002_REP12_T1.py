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

def test_position_out_of_bounds():
    assert split_by_positions("Hello", [10]) == ["Hello"]

def test_consecutive_positions():
    assert split_by_positions("Hello World", [0, 6, 11]) == ["", "Hello ", "World"]

def test_position_at_start():
    assert split_by_positions("Hello World", [0, 6]) == ["", "Hello"]

def test_position_at_end():
    assert split_by_positions("Hello World", [11]) == ["Hello World", ""]

test_standard_input()
test_empty_input()
test_empty_positions()
test_position_out_of_bounds()
test_consecutive_positions()
test_position_at_start()
test_position_at_end()