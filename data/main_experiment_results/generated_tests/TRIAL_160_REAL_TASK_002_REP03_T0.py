from typing import List

def test_split_by_positions_standard_input():
    line = "   Hello   World  "
    positions = [3, 9]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_empty_line():
    line = ""
    positions = [0, 5]
    expected_output = ["", ""]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_empty_positions():
    line = "Hello World"
    positions = []
    expected_output = []
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_out_of_bounds_positions():
    line = "Hello World"
    positions = [-1, 15]
    expected_output = ["Hello World", ""]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_consecutive_positions():
    line = "Hello World"
    positions = [0, 0, 5]
    expected_output = ["", "Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_last_position_at_end_of_line():
    line = "Hello World"
    positions = [0, 5, 11]
    expected_output = ["Hello", "World", ""]
    assert split_by_positions(line, positions) == expected_output