def test_partial_overlap():
    assert check_half_open_overlap(1, 5, 3, 7) == True  # Partial overlap

def test_no_overlap():
    assert check_half_open_overlap(1, 5, 6, 7) == False  # No overlap

def test_adjacent_intervals():
    assert check_half_open_overlap(1, 5, 5, 7) == False  # Adjacent, no overlap

def test_fully_contained():
    assert check_half_open_overlap(2, 6, 3, 5) == False  # Fully contained, no strict overlap

def test_reverse_partial_overlap():
    assert check_half_open_overlap(3, 7, 1, 5) == True  # Reverse partial overlap

def test_same_intervals():
    assert check_half_open_overlap(1, 5, 1, 5) == False  # Same intervals, no strict overlap