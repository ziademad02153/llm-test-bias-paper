from typing import List

def test_standard_input():
    assert split_by_positions("  Hello  World  ", [3, 10]) == ["Hello", "World"]

def test_empty_input():
    assert split_by_positions("", [1, 2]) == ["", ""]

def test_empty_positions():
    assert split_by_positions("Hello World", []) == ["Hello World"]

def test_positions_out_of_bounds():
    assert split_by_positions("Hello", [10]) == ["Hello"]

def test_consecutive_positions():
    assert split_by_positions("Hello World", [0, 0, 6]) == ["", "", "World"]

def test_positions_at_end_of_line():
    assert split_by_positions("Hello World", [0, 11]) == ["Hello World", ""]

def test_negative_positions():
    try:
        split_by_positions("Hello World", [-1, 6])
        assert False, "Expected ValueError for negative positions"
    except ValueError:
        pass

def test_non_integer_positions():
    try:
        split_by_positions("Hello World", [0, 'a'])
        assert False, "Expected TypeError for non-integer positions"
    except TypeError:
        pass