from typing import List

def test_standard_input():
    line = "  Hello  World  "
    positions = [3, 9]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_empty_input():
    line = ""
    positions = [1, 3]
    expected_output = ["", ""]
    assert split_by_positions(line, positions) == expected_output

def test_out_of_bounds_positions():
    line = "Hello World"
    positions = [-1, 15]
    expected_output = ["", "Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_single_position():
    line = "Hello World"
    positions = [6]
    expected_output = ["World"]
    assert split_by_positions(line, positions) == expected_output

def test_no_positions():
    line = "Hello World"
    positions = []
    expected_output = ["Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_consecutive_positions():
    line = "Hello World"
    positions = [0, 0, 6]
    expected_output = ["", "Hello", "World"]
    assert split_by_positions(line, positions) == expected_output