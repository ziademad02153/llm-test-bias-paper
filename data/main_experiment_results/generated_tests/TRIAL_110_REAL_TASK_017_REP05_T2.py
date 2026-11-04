def test_empty_timestamps_within_limit():
    """Test when timestamps list is empty and current time is within limit."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 60.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_exact_limit_no_eviction():
    """Test when exactly at limit and no timestamps need eviction."""
    timestamps = [90.0, 95.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 105.0, 3, 20.0)
    assert allowed is False
    assert updated_timestamps == [95.0, 100.0, 105.0]

def test_partial_eviction_within_limit():
    """Test partial eviction of old timestamps with remaining within limit."""
    timestamps = [10.0, 20.0, 30.0, 40.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 50.0, 5, 25.0)
    assert allowed is True
    assert updated_timestamps == [30.0, 40.0, 50.0]

def test_all_evicted_below_limit():
    """Test all timestamps are evicted, allowing new current time."""
    timestamps = [10.0, 20.0, 30.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 50.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_limit_zero_always_rejected():
    """Test that with limit=0, any request is rejected."""
    timestamps = []
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 50.0, 0, 10.0)
    assert allowed is False
    assert updated_timestamps == []