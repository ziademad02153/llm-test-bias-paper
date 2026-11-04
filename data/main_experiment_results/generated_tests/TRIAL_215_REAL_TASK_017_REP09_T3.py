def test_empty_timestamps_allows_request():
    """Empty timestamps should always allow the request and append current_time."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]

def test_within_limit_allows_request():
    """Timestamps within the limit should allow the request and append current_time."""
    timestamps = [95.0, 96.0, 97.0]
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [95.0, 96.0, 97.0, 100.0]

def test_exceeds_limit_rejects_request():
    """Timestamps exceeding the limit should reject the request and evict old entries."""
    timestamps = [91.0, 95.0, 96.0, 97.0, 98.0]  # 5 requests in last 10 seconds (91.0 is expired)
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert new_timestamps == [95.0, 96.0, 97.0, 98.0]  # 91.0 evicted, but current_time not appended

def test_edge_case_exact_window_boundary():
    """Timestamps exactly at the window boundary should be evicted."""
    timestamps = [90.0, 91.0]  # 90.0 is exactly at boundary (current_time=100.0, window=10.0)
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 2, 10.0)
    assert result is True
    assert new_timestamps == [91.0, 100.0]  # 90.0 evicted

def test_limit_zero_rejects_all_requests():
    """Zero limit should reject all requests regardless of timestamps."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 0, 10.0)
    assert result is False
    assert new_timestamps == []

def test_evicts_multiple_expired_entries():
    """Multiple expired timestamps should be evicted, leaving only valid ones."""
    timestamps = [85.0, 89.0, 95.0, 99.0]  # 85.0 and 89.0 expired (current_time=100.0, window=10.0)
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [95.0, 99.0, 100.0]