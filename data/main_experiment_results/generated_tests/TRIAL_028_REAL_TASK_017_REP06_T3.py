def test_empty_timestamps_allows_request():
    """Test that an empty timestamps list allows the request and appends current_time."""
    result, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed and current_time is appended."""
    timestamps = [95.0, 96.0, 97.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert updated_timestamps == [95.0, 96.0, 97.0, 100.0]

def test_exceeds_limit_rejects_request():
    """Test that a request exceeding the limit is rejected and expired timestamps are evicted."""
    timestamps = [91.0, 95.0, 96.0, 97.0, 98.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert updated_timestamps == [95.0, 96.0, 97.0, 98.0]  # 91.0 is evicted

def test_all_timestamps_expired_resets_window():
    """Test that all expired timestamps are evicted, allowing a new request."""
    timestamps = [89.0, 90.0]  # All older than window (current_time=100.0, window=10.0)
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert updated_timestamps == [100.0]

def test_exact_limit_boundary_behavior():
    """Test exact boundary case where oldest timestamp is exactly at the window edge."""
    timestamps = [90.0, 95.0, 96.0, 97.0, 98.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False  # 90.0 is exactly at the boundary (not evicted yet)
    assert updated_timestamps == [90.0, 95.0, 96.0, 97.0, 98.0]

def test_zero_window_rejects_all_requests():
    """Test that a zero-length window rejects all requests (except empty case)."""
    timestamps = [100.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 0.0)
    assert result is False
    assert updated_timestamps == [100.0]  # No eviction, but request denied