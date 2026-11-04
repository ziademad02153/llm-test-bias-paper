from typing import List

def test_standard_input():
    line = "   hello   world  python  "
    positions = [3, 10, 17]
    expected_output = ["hello", "world", "python"]
    assert split_by_positions(line, positions) == expected_output

def test_empty_input():
    line = ""
    positions = [1, 3, 5]
    expected_output = ["", "", ""]
    assert split_by_positions(line, positions) == expected_output

def test_empty_positions():
    line = "hello world"
    positions = []
    expected_output = []
    assert split_by_positions(line, positions) == expected_output

def test_out_of_bounds_positions():
    line = "hello world"
    positions = [10, 15, 20]
    expected_output = ["", "", ""]
    assert split_by_positions(line, positions) == expected_output

def test_negative_positions():
    line = "hello world"
    positions = [-1, 3, 5]
    try:
        split_by_positions(line, positions)
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        pass

def test_non_integer_positions():
    line = "hello world"
    positions = [1.5, 3, 5]
    try:
        split_by_positions(line, positions)
        assert False, "Expected TypeError for non-integer positions"
    except TypeError:
        pass