def test_half_open_overlap_standard_case():
    assert check_half_open_overlap(1, 5, 3, 7) == True

def test_half_open_overlap_no_overlap():
    assert check_half_open_overlap(1, 3, 4, 7) == False

def test_half_open_overlap_edge_case_equal_start():
    assert check_half_open_overlap(1, 5, 1, 7) == True

def test_half_open_overlap_edge_case_equal_end():
    assert check_half_open_overlap(1, 5, 3, 5) == True

def test_half_open_overlap_invalid_input():
    try:
        check_half_open_overlap("a", 5, 3, 7)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_half_open_overlap_empty_interval():
    assert check_half_open_overlap(1, 1, 3, 7) == False