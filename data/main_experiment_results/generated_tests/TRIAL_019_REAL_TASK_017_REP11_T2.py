def test_empty_timestamps_within_limit():
    """Test with empty timestamps and current time within limit."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_exact_limit_no_expiry():
    """Test when exactly at limit with no expired timestamps."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]  # 5 timestamps (limit=5)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == timestamps  # No change (current_time not appended)

def test_expired_timestamps_evicted():
    """Test that expired timestamps are evicted and new one is appended."""
    timestamps = [90.0, 95.0, 96.0]  # 90.0 is expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [95.0, 96.0, 100.0]

def test_limit_reached_after_eviction():
    """Test limit is still reached after evicting expired timestamps."""
    timestamps = [90.0, 91.0, 95.0, 96.0, 97.0]  # 90.0 and 91.0 expire, leaving 3
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 3, 10.0)
    assert allowed is False  # Because after eviction, len=3 (== limit)
    assert updated_timestamps == [95.0, 96.0, 97.0]  # No append

def test_edge_case_window_boundary():
    """Test timestamps exactly at the window boundary are evicted."""
    timestamps = [90.0, 100.0]  # 90.0 is exactly expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0, 100.0]  # 90.0 evicted, 100.0 appended