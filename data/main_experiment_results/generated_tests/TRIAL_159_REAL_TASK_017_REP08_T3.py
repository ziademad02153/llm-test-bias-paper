def test_empty_timestamps_allows_request():
    """Test that an empty timestamps list allows the request and appends current_time."""
    result, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed and current_time is appended."""
    timestamps = [95.0, 97.0, 99.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert updated_timestamps == [95.0, 97.0, 99.0, 100.0]

def test_exceeds_limit_rejects_request():
    """Test that a request exceeding the limit is rejected and old timestamps are evicted."""
    timestamps = [91.0, 95.0, 97.0, 99.0, 100.0]
    current_time = 101.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert updated_timestamps == [95.0, 97.0, 99.0, 100.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [89.0, 91.0, 95.0, 99.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 2, 10.0)
    assert result is True
    assert updated_timestamps == [95.0, 99.0, 100.0]

def test_zero_limit_rejects_all_requests():
    """Test that a zero limit rejects all requests regardless of timestamps."""
    timestamps = []
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 0, 10.0)
    assert result is False
    assert updated_timestamps == []

def test_window_size_zero_allows_unlimited_requests():
    """Test that a zero window size allows unlimited requests (no timestamps expire)."""
    timestamps = [90.0, 95.0, 100.0]
    current_time = 100.0
    result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 2, 0.0)
    assert result is False  # Because the limit (2) is exceeded by the existing 3 timestamps
    assert updated_timestamps == [90.0, 95.0, 100.0]