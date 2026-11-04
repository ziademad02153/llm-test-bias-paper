def test_standard_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True
    assert check_half_open_overlap(1, 5, 0, 3) == True
    assert check_half_open_overlap(1, 5, 2, 4) == True

def test_no_overlap():
    assert check_half_open_overlap(1, 5, 5, 7) == False
    assert check_half_open_overlap(1, 5, 6, 7) == False
    assert check_half_open_overlap(1, 5, 8, 10) == False

def test_edge_cases():
    assert check_half_open_overlap(1, 1, 1, 1) == False
    assert check_half_open_overlap(1, 5, 1, 5) == False
    assert check_half_open_overlap(1, 10, 1, 10) == False

def test_invalid_inputs():
    try:
        check_half_open_overlap("a", 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        check_half_open_overlap(1, 5, None, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_unordered_inputs():
    assert check_half_open_overlap(5, 1, 3, 7) == False
    assert check_half_open_overlap(1, 5, 7, 3) == False
    assert check_half_open_overlap(5, 1, 7, 3) == False

def test_large_inputs():
    assert check_half_open_overlap(1000000, 2000000, 1500000, 2500000) == True
    assert check_half_open_overlap(1000000, 2000000, 2500000, 3000000) == False