from typing import List

def test_split_by_positions_standard_input():
    assert split_by_positions("  Hello  World  ", [3, 10]) == ["Hello", "World"]

def test_split_by_positions_empty_input():
    assert split_by_positions("", [1, 2]) == ["", ""]

def test_split_by_positions_empty_positions():
    assert split_by_positions("Hello World", []) == ["Hello World"]

def test_split_by_positions_out_of_bounds_positions():
    assert split_by_positions("Hello World", [100, 200]) == ["", ""]

def test_split_by_positions_negative_positions():
    try:
        split_by_positions("Hello World", [-1, 2])
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        pass

def test_split_by_positions_non_integer_positions():
    try:
        split_by_positions("Hello World", [1.5, 2])
        assert False, "Expected TypeError for non-integer positions"
    except TypeError:
        pass