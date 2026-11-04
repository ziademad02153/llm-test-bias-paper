def test_empty_timestamps_within_limit():
    """Test when timestamps list is empty and current time is within limit."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_exact_limit_no_expiry():
    """Test when timestamps exactly match limit but none are expired."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == timestamps  # No change since limit reached

def test_partial_expiry_within_limit():
    """Test when some timestamps are expired and current time is within limit."""
    timestamps = [90.0, 95.0, 96.0, 97.0]  # 90.0 is expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [95.0, 96.0, 97.0, 100.0]

def test_all_expired_resets_limit():
    """Test when all timestamps are expired, allowing current time."""
    timestamps = [80.0, 85.0, 89.0]  # All expired (current_time=100.0, window=10.0)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 3, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_zero_limit_always_rejected():
    """Test when limit is zero, current time is always rejected."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 0, 10.0)
    assert allowed is False
    assert updated_timestamps == []

def test_window_size_zero_always_rejected():
    """Test when window size is zero, all timestamps are considered expired."""
    timestamps = [99.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 0.0)
    assert allowed is False
    assert updated_timestamps == []