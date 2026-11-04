def test_overlap(): 
    assert check_half_open_overlap(1, 5, 3, 7) == True
    assert check_half_open_overlap(1, 5, 6, 7) == False
    assert check_half_open_overlap(1, 5, 0, 3) == True

def test_edge_cases():
    assert check_half_open_overlap(1, 1, 1, 2) == False
    assert check_half_open_overlap(1, 2, 1, 1) == False
    assert check_half_open_overlap(1, 2, 2, 3) == False

def test_invalid_inputs():
    try:
        check_half_open_overlap('a', 5, 3, 7)
        assert False, "Expected TypeError for non-integer input"
    except TypeError:
        pass

    try:
        check_half_open_overlap(5, 3, 3, 7)
        assert False, "Expected ValueError for invalid interval"
    except ValueError:
        pass

def test_equal_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False
    assert check_half_open_overlap(1, 5, 1, 6) == True
    assert check_half_open_overlap(1, 6, 1, 5) == True