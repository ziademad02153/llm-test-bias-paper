from typing import List

def test_standard_input():
    assert split_by_positions("  Hello  World  ", [3, 10]) == ["Hello", "World"]

def test_empty_input():
    assert split_by_positions("", []) == []

def test_empty_line():
    assert split_by_positions("", [1, 2]) == ["", ""]

def test_no_positions():
    assert split_by_positions("Hello World", []) == []

def test_single_position():
    assert split_by_positions("Hello World", [6]) == ["Hello", "World"]

def test_out_of_bounds_position():
    assert split_by_positions("Hello", [10]) == ["Hello"]