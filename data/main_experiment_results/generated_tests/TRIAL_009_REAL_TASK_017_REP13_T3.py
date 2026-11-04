def test_empty_timestamps_under_limit():
    """Test with empty timestamps and under limit should allow and append current_time."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]

def test_within_limit_no_eviction():
    """Test timestamps within window and under limit should allow and append current_time."""
    timestamps = [95.0, 96.0, 97.0]
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [95.0, 96.0, 97.0, 100.0]

def test_exceeds_limit():
    """Test timestamps within window exceeding limit should deny and not append current_time."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert new_timestamps == [95.0, 96.0, 97.0, 98.0, 99.0]

def test_evict_expired_timestamps():
    """Test evicting expired timestamps and allowing new request."""
    timestamps = [89.0, 90.0, 91.0, 99.0]  # 89.0 and 90.0 are expired for window=10.0 at current_time=100.0
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [91.0, 99.0, 100.0]

def test_exact_limit_boundary():
    """Test exactly at the limit boundary should deny new request."""
    timestamps = [90.0, 91.0, 92.0, 93.0, 94.0]  # Exactly 5 requests in last 10 seconds
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert new_timestamps == [90.0, 91.0, 92.0, 93.0, 94.0]

def test_all_expired_timestamps():
    """Test all timestamps expired should allow and append current_time."""
    timestamps = [80.0, 85.0, 89.0]  # All expired for window=10.0 at current_time=100.0
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]