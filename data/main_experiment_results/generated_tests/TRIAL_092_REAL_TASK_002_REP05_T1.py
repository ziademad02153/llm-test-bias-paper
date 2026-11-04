from typing import List

def test_standard_input():
    line = "   Hello   World  "
    positions = [3, 10]
    expected_output = ["Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_empty_input():
    line = ""
    positions = [0, 5]
    expected_output = []
    assert split_by_positions(line, positions) == expected_output

def test_empty_positions():
    line = "Hello World"
    positions = []
    expected_output = ["Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_out_of_bounds_positions():
    line = "Hello World"
    positions = [10, 20]
    expected_output = ["Hello World"]
    assert split_by_positions(line, positions) == expected_output

def test_consecutive_positions():
    line = "Hello World"
    positions = [0, 0, 5]
    expected_output = ["", "Hello", "World"]
    assert split_by_positions(line, positions) == expected_output

def test_negative_positions():
    line = "Hello World"
    positions = [-1, 5]
    try:
        split_by_positions(line, positions)
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        assert True
    except Exception as e:
        assert False, f"Expected ValueError, got {type(e).__name__}"