def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True  # Partial overlap [1,5) and [3,7)

def test_no_overlap_adjacent():
    assert check_half_open_overlap(1, 5, 5, 7) == False  # No overlap, adjacent intervals [1,5) and [5,7)

def test_partial_overlap_reverse():
    assert check_half_open_overlap(3, 7, 1, 5) == True  # Partial overlap [3,7) and [1,5)

def test_no_overlap_separate():
    assert check_half_open_overlap(1, 5, 6, 7) == False  # No overlap, separate intervals [1,5) and [6,7)

def test_fully_contained_no_strict_overlap():
    assert check_half_open_overlap(1, 5, 2, 4) == False  # Fully contained, no strict overlap [1,5) and [2,4)

def test_fully_contained_reverse_no_strict_overlap():
    assert check_half_open_overlap(2, 4, 1, 5) == False  # Fully contained, no strict overlap [2,4) and [1,5)