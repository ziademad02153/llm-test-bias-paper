def test_partial_overlap():
    """Test intervals that partially overlap."""
    assert check_half_open_overlap(1, 5, 3, 7) == True

def test_no_overlap():
    """Test intervals that do not overlap."""
    assert check_half_open_overlap(1, 5, 6, 8) == False

def test_adjacent_intervals():
    """Test intervals that are adjacent but do not overlap."""
    assert check_half_open_overlap(1, 5, 5, 7) == False

def test_fully_contained():
    """Test one interval fully contained within another (should return False as per spec)."""
    assert check_half_open_overlap(2, 8, 3, 6) == False

def test_reverse_order():
    """Test intervals where the second interval starts before the first."""
    assert check_half_open_overlap(4, 7, 2, 5) == True

def test_same_intervals():
    """Test identical intervals (should return True as they overlap)."""
    assert check_half_open_overlap(3, 6, 3, 6) == True