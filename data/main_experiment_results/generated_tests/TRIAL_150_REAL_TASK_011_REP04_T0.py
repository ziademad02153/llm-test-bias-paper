def test_overlap(): 
    assert check_half_open_overlap(1, 5, 3, 7) == True
    assert check_half_open_overlap(1, 5, 5, 7) == False
    assert check_half_open_overlap(1, 5, 0, 3) == True

def test_no_overlap():
    assert check_half_open_overlap(1, 3, 4, 6) == False
    assert check_half_open_overlap(1, 3, 3, 6) == False

def test_edge_cases():
    assert check_half_open_overlap(1, 1, 1, 1) == False
    assert check_half_open_overlap(1, 10, 1, 10) == True

def test_invalid_input():
    try:
        check_half_open_overlap('a', 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(5, 'b', 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(5, 3, 'c', 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(5, 3, 7, 'd')
        assert False, "Expected TypeError"
    except TypeError:
        pass