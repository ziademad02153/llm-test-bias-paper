# Test standard intersection
def test_standard_intersection():
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)

# Test intersection with unbounded endpoints
def test_unbounded_intersection():
    assert intersect_intervals(1, None, 3, 7) == (3, 7)

# Test non-intersecting intervals
def test_non_intersecting():
    assert intersect_intervals(1, 3, 5, 7) is None

# Test empty intervals
def test_empty_intervals():
    assert intersect_intervals(None, None, 1, 5) is None
    assert intersect_intervals(1, 5, None, None) is None

# Test identical intervals
def test_identical_intervals():
    assert intersect_intervals(1, 5, 1, 5) == (1, 5)

# Test invalid input (not applicable in this case, as the function signature allows None)