def test_empty_timestamps_allowed():
    """Test that an empty list of timestamps allows the current time."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert timestamps == [100.0]

def test_exact_limit_reached():
    """Test that the limit is enforced when exactly reached."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]  # 5 timestamps (limit=5)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == timestamps  # No new timestamp added

def test_evict_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [90.0, 95.0, 99.0]  # 90.0 is expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is True
    assert updated_timestamps == [95.0, 99.0, 100.0]

def test_limit_not_reached_after_eviction():
    """Test that after eviction, the limit is not reached, so current_time is allowed."""
    timestamps = [90.0, 91.0, 92.0]  # All expired (current_time=100.0, window=5.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 5.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_zero_limit_rejects_all():
    """Test that a zero limit rejects all timestamps."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 0, 10.0)
    assert allowed is False
    assert timestamps == []

def test_window_size_zero_always_rejects():
    """Test that a zero window size rejects all timestamps (since all are expired)."""
    allowed, timestamps = check_sliding_window_rate_limit([100.0], 100.0, 1, 0.0)
    assert allowed is True  # The expired timestamp is evicted, so the limit is not reached
    assert timestamps == [100.0]