def test_empty_timestamps_within_limit():
    """Test that an empty list of timestamps allows the current time and adds it."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_timestamps_within_window_and_limit():
    """Test that timestamps within the window and under the limit allow the current time."""
    timestamps = [95.0, 96.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 4
    assert 100.0 in updated_timestamps

def test_timestamps_exceeding_limit():
    """Test that timestamps exceeding the limit disallow the current time."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_evict_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [90.0, 95.0, 99.0]  # 90.0 is expired if current_time is 100.0 and window is 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 2
    assert 90.0 not in updated_timestamps
    assert 100.0 in updated_timestamps

def test_exact_limit_with_expired_timestamps():
    """Test that exactly reaching the limit after eviction works correctly."""
    timestamps = [91.0, 92.0, 93.0, 94.0, 95.0]  # All within 10.0 window if current_time is 100.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_zero_limit():
    """Test that a zero limit always disallows the current time."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 0, 10.0)
    assert allowed is False
    assert updated_timestamps == []