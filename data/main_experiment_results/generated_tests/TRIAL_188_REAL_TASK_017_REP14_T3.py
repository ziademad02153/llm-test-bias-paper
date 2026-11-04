def test_empty_timestamps_within_limit():
    """Test with empty timestamps and within rate limit."""
    result, new_timestamps = check_sliding_window_rate_limit([], 10.0, 2, 5.0)
    assert result is True
    assert new_timestamps == [10.0]

def test_no_eviction_within_window():
    """Test no eviction when timestamps are within the window."""
    timestamps = [1.0, 2.0, 3.0]
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 4.0, 5, 5.0)
    assert result is True
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0]

def test_eviction_outside_window():
    """Test eviction of timestamps outside the window."""
    timestamps = [1.0, 6.0, 7.0]  # 1.0 is outside window (current_time=10.0, window=5.0)
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 10.0, 3, 5.0)
    assert result is True
    assert new_timestamps == [6.0, 7.0, 10.0]

def test_rate_limit_exceeded():
    """Test when rate limit is exceeded."""
    timestamps = [1.0, 2.0, 3.0]
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 4.0, 3, 5.0)
    assert result is False
    assert new_timestamps == [1.0, 2.0, 3.0]  # current_time not appended

def test_edge_case_empty_timestamps_at_limit():
    """Test empty timestamps when limit is 0 (always reject)."""
    result, new_timestamps = check_sliding_window_rate_limit([], 10.0, 0, 5.0)
    assert result is False
    assert new_timestamps == []

def test_edge_case_window_zero():
    """Test edge case where window_seconds is 0 (all timestamps are evicted)."""
    timestamps = [1.0, 2.0, 3.0]
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, 4.0, 2, 0.0)
    assert result is True
    assert new_timestamps == [4.0]