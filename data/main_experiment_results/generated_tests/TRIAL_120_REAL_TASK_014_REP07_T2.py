# Test standard inputs
def test_standard_inputs():
    assert compute_exponential_backoff_sequence(3) == [1.0, 2.0, 4.0]
    assert compute_exponential_backoff_sequence(3, base=3.0, factor=2.0) == [2.0, 6.0, 18.0]
    assert compute_exponential_backoff_sequence(3, max_value=3.0) == [1.0, 2.0]

# Test edge cases
def test_edge_cases():
    assert compute_exponential_backoff_sequence(0) == []
    assert compute_exponential_backoff_sequence(1, base=1.0, factor=1.0) == [1.0]
    assert compute_exponential_backoff_sequence(3, base=1.0, factor=1.0, max_value=1.0) == [1.0, 1.0, 1.0]

# Test max_value bounding
def test_max_value_bounding():
    assert compute_exponential_backoff_sequence(5, max_value=10.0) == [1.0, 2.0, 4.0, 8.0]
    assert compute_exponential_backoff_sequence(5, base=3.0, factor=2.0, max_value=20.0) == [2.0, 6.0, 18.0]

# Test negative inputs (should raise TypeError)
def test_negative_inputs():
    try:
        compute_exponential_backoff_sequence(-1)
        assert False, "Expected TypeError for negative attempts"
    except TypeError:
        pass

# Test invalid types (should raise TypeError)
def test_invalid_types():
    try:
        compute_exponential_backoff_sequence("3")
        assert False, "Expected TypeError for non-integer attempts"
    except TypeError:
        pass
    try:
        compute_exponential_backoff_sequence(3, base="2.0")
        assert False, "Expected TypeError for non-float base"
    except TypeError:
        pass