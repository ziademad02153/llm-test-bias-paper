def test_empty_timestamps_allowed():
    """Test that an empty list of timestamps allows the current time to be added."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 2, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_within_limit_allowed():
    """Test that timestamps within the limit are allowed."""
    timestamps = [90.0, 95.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 3, 10.0)
    assert allowed is True
    assert updated_timestamps == [90.0, 95.0, 100.0]

def test_exceeds_limit_rejected():
    """Test that exceeding the limit results in rejection."""
    timestamps = [90.0, 95.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 3, 10.0)
    assert allowed is False
    assert updated_timestamps == [90.0, 95.0, 99.0]  # No new timestamp added

def test_evict_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [80.0, 90.0, 95.0]  # 80.0 is expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is False  # 90.0 and 95.0 are still within the window (len=2, limit=2)
    assert updated_timestamps == [90.0, 95.0]

def test_exact_limit_boundary():
    """Test the boundary case where the number of timestamps equals the limit."""
    timestamps = [90.0, 95.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is False
    assert updated_timestamps == [90.0, 95.0]  # No new timestamp added

def test_window_size_zero():
    """Test edge case where window size is zero (all timestamps are considered expired)."""
    timestamps = [90.0, 95.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 0.0)
    assert allowed is True  # All expired, so current_time is allowed
    assert updated_timestamps == [100.0]