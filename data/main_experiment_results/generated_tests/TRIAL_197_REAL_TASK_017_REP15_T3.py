def test_empty_timestamps_under_limit():
    """Test with empty timestamps when under limit - should allow and add current_time."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]

def test_exact_limit_no_eviction():
    """Test when exactly at limit but all timestamps are within window - should reject."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert result is False
    assert new_timestamps == timestamps  # No change

def test_partial_eviction_under_limit():
    """Test with some expired timestamps putting under limit - should allow and add current_time."""
    timestamps = [89.0, 90.0, 91.0, 99.0, 100.0]  # First two should be evicted
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 101.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [91.0, 99.0, 100.0, 101.0]

def test_all_expired_resets_window():
    """Test when all timestamps are expired - should allow and start new window."""
    timestamps = [89.0, 90.0, 91.0]  # All expired for window=10 at current_time=100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]

def test_zero_limit_rejects_all():
    """Test with zero limit - should always reject."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 0, 10.0)
    assert result is False
    assert new_timestamps == []

def test_window_size_zero_always_rejects():
    """Test with zero window size - should reject all (window effectively instantaneous)."""
    result, new_timestamps = check_sliding_window_rate_limit([100.0], 100.0, 1, 0.0)
    assert result is False
    assert new_timestamps == [100.0]