def test_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True
    assert check_half_open_overlap(1, 5, 0, 3) == True
    assert check_half_open_overlap(1, 5, 2, 4) == True

def test_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 7) == False
    assert check_half_open_overlap(1, 5, 6, 7) == False
    assert check_half_open_overlap(1, 5, 7, 10) == False

def test_edge_cases():
    assert check_half_open_overlap(1, 1, 1, 1) == False
    assert check_half_open_overlap(1, 10, 1, 10) == False
    assert check_half_open_overlap(1, 5, 1, 5) == False

def test_invalid_inputs():
    try:
        check_half_open_overlap("a", 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(1, "b", 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(1, 5, "c", 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(1, 5, 3, "d")
        assert False, "Expected TypeError"
    except TypeError:
        pass

test_overlap()
test_no_overlap()
test_edge_cases()
test_invalid_inputs()