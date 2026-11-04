Here is a comprehensive suite of unit tests for the `intersect_intervals` function:

```python
def test_intersect_bounded_intervals():
    # Test intersection of two bounded intervals that overlap
    assert intersect_intervals(1, 5, 3, 7) == (3, 5)
    # Test intersection of two bounded intervals that don't overlap
    assert intersect_intervals(1, 3, 5, 7) is None
    # Test intersection where one interval is entirely within the other
    assert intersect_intervals(2, 6, 3, 5) == (3, 5)

def test_intersect_unbounded_start():
    # Test intersection with one interval unbounded on the start (None)
    assert intersect_intervals(None, 5, 3, 7) == (3, 5)
    # Test intersection with both intervals unbounded on the start
    assert intersect_intervals(None, 5, None, 7) == (None, 5)

def test_intersect_unbounded_end():
    # Test intersection with one interval unbounded on the end (None)
    assert intersect_intervals(3, None, 1, 5) == (3, 5)
    # Test intersection with both intervals unbounded on the end
    assert intersect_intervals(3, None, 1, None) == (3, None)

def test_intersect_fully_unbounded():
    # Test intersection where one interval is fully unbounded
    assert intersect_intervals(None, None, 2, 4) == (2, 4)
    # Test intersection where both intervals are fully unbounded
    assert intersect_intervals(None, None, None, None) == (None, None)

def test_intersect_edge_cases():
    # Test intersection where intervals are adjacent but don't overlap
    assert intersect_intervals(1, 2, 2, 3) is None
    # Test intersection where intervals are single points and overlap
    assert intersect_intervals(2, 2, 2, 2) == (2, 2)
    # Test intersection where one interval is a point and doesn't overlap
    assert intersect_intervals(2, 2, 3, 3) is None