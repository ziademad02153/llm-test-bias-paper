from typing import List

def test_standard_input():
    line = "   field1   field2   field3  "
    positions = [3, 10, 17]
    expected_output = ["field1", "field2", "field3"]
    assert split_by_positions(line, positions) == expected_output

def test_empty_input():
    line = ""
    positions = [0, 5]
    expected_output = ["", ""]
    assert split_by_positions(line, positions) == expected_output

def test_empty_positions():
    line = "field1 field2 field3"
    positions = []
    expected_output = []
    assert split_by_positions(line, positions) == expected_output

def test_out_of_bounds_positions():
    line = "field1 field2 field3"
    positions = [-1, 10, 20]
    expected_output = ["", "field1 field2", "field3"]
    assert split_by_positions(line, positions) == expected_output

def test_positions_at_end_of_line():
    line = "field1 field2 field3"
    positions = [0, 6, len(line)]
    expected_output = ["field1", "field2 field3", ""]
    assert split_by_positions(line, positions) == expected_output

def test_consecutive_positions():
    line = "field1 field2 field3"
    positions = [0, 0, 6]
    expected_output = ["", "field1", "field2 field3"]
    assert split_by_positions(line, positions) == expected_output