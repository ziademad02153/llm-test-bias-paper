from typing import List

def test_split_by_positions_standard_input():
    line = "  Hello  World  "
    positions = [3, 9]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_empty_input():
    line = ""
    positions = [1, 2]
    expected_output = []
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_empty_positions():
    line = "Hello World"
    positions = []
    expected_output = ["Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_out_of_bounds_positions():
    line = "Hello World"
    positions = [100, 200]
    expected_output = ["Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_consecutive_positions():
    line = "Hello World"
    positions = [0, 0, 5]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_negative_positions():
    line = "Hello World"
    positions = [-1, 5]
    try:
        split_by_positions(line, positions)
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        assert True
    except Exception:
        assert False, "Expected ValueError for negative positions"

# Test with actual implementation to check for ValueError
def split_by_positions(line: str, positions: List[int]) -> List[str]:
    if any(pos < 0 for pos in positions):
        raise ValueError("Positions cannot be negative")
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