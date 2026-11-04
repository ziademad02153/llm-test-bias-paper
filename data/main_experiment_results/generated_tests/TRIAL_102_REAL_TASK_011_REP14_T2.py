def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True

def test_no_overlap():
    assert check_half_open_overlap(1, 5, 6, 7) == False

def test_touching_intervals():
    assert check_half_open_overlap(1, 5, 5, 7) == False

def test_fully_contained_overlap():
    assert check_half_open_overlap(2, 6, 3, 5) == False

def test_reverse_order_overlap():
    assert check_half_open_overlap(3, 7, 1, 5) == True

def test_same_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False