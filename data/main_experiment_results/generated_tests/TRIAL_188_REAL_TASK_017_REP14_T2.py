def test_below_limit_allows_and_appends():
    """Test that a request below the limit is allowed and timestamp is appended."""
    timestamps = [1.0, 2.0]
    current_time = 3.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0, 2.0, 3.0]

def test_at_limit_rejects_and_does_not_append():
    """Test that a request at the limit is rejected and timestamp is not appended."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert updated_timestamps == [1.0, 2.0, 3.0]

def test_expired_timestamps_are_evicted():
    """Test that expired timestamps are evicted from the window."""
    timestamps = [1.0, 2.0, 11.0]  # 11.0 is expired if current_time is 12.0 and window is 10.0
    current_time = 12.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [2.0, 12.0]

def test_empty_timestamps_allows_first_request():
    """Test that an empty list of timestamps allows the first request."""
    timestamps = []
    current_time = 1.0
    limit = 1
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0]

def test_window_boundary_evicts_correctly():
    """Test that timestamps exactly at the window boundary are evicted."""
    timestamps = [1.0, 10.0]  # 1.0 is exactly expired if current_time is 11.0 and window is 10.0
    current_time = 11.0
    limit = 2
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [10.0, 11.0]