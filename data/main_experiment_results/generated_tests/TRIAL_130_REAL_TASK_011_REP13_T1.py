def test_standard_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True
    assert check_half_open_overlap(1, 5, 0, 3) == True

def test_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 7) == False
    assert check_half_open_overlap(1, 5, 6, 7) == False

def test_edge_cases():
    assert check_half_open_overlap(1, 1, 1, 1) == False
    assert check_half_open_overlap(1, 5, 1, 5) == False

def test_invalid_input():
    try:
        check_half_open_overlap("a", 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_unordered_input():
    assert check_half_open_overlap(5, 1, 3, 7) == False
    assert check_half_open_overlap(1, 5, 7, 3) == False

def test_equal_bounds():
    assert check_half_open_overlap(1, 5, 1, 5) == False
    assert check_half_open_overlap(1, 5, 5, 5) == False