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

def test_out_of_bounds_positions():
    assert split_by_positions("Hello", [10]) == ["Hello"]

def test_consecutive_positions():
    assert split_by_positions("Hello World", [0, 6, 11]) == ["", "Hello", "World"]

def test_positions_with_whitespace():
    assert split_by_positions("   Hello   World   ", [3, 9, 16]) == ["Hello", "World", ""]

def test_positions_with_empty_fields():
    assert split_by_positions("Hello World", [0, 0, 6, 6, 11]) == ["", "", "Hello", "", "World"]

def test_negative_positions():
    try:
        split_by_positions("Hello World", [-1])
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        assert True

def test_non_integer_positions():
    try:
        split_by_positions("Hello World", [1.5])
        assert False, "Expected TypeError for non-integer positions"
    except TypeError:
        assert True

def test_non_list_positions():
    try:
        split_by_positions("Hello World", "123")
        assert False, "Expected TypeError for non-list positions"
    except TypeError:
        assert True