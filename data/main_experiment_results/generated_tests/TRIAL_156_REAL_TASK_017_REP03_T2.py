def test_empty_timestamps_within_limit():
    """Test with empty timestamps and within rate limit."""
    allowed, new_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 60.0)
    assert allowed is True
    assert new_timestamps == [100.0]

def test_exact_limit_no_eviction():
    """Test when exactly at limit and no eviction needed."""
    timestamps = [90.0, 95.0, 100.0]
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, 105.0, 3, 20.0)
    assert allowed is False
    assert new_timestamps == [95.0, 100.0, 105.0]

def test_partial_eviction_within_limit():
    """Test partial eviction of old timestamps and within limit."""
    timestamps = [10.0, 20.0, 30.0, 40.0]
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, 50.0, 5, 15.0)
    assert allowed is True
    assert new_timestamps == [40.0, 50.0]

def test_all_evicted_below_limit():
    """Test all timestamps evicted due to being outside window."""
    timestamps = [10.0, 20.0, 30.0]
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 50.0)
    assert allowed is True
    assert new_timestamps == [100.0]

def test_at_limit_with_eviction():
    """Test at limit but some timestamps are evicted."""
    timestamps = [40.0, 50.0, 60.0, 70.0]
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, 80.0, 3, 30.0)
    assert allowed is False
    assert new_timestamps == [50.0, 60.0, 70.0, 80.0]