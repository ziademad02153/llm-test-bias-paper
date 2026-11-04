from typing import List

def test_split_by_positions_standard_input():
    line = "  Hello   World  "
    positions = [3, 10]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_empty_input():
    line = ""
    positions = [3, 10]
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
    expected_output = ["", "Hello"]
    assert split_by_positions(line, positions) == expected_output

def test_split_by_positions_negative_positions():
    line = "Hello World"
    positions = [-1, 5]
    try:
        split_by_positions(line, positions)
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        pass