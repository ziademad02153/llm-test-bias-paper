def test_within_limit_returns_true_and_appends_timestamp():
    """Test that when within limit, returns True and appends current_time."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 10.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0]

def test_exceeds_limit_returns_false_and_does_not_append():
    """Test that when exceeding limit, returns False and does not append current_time."""
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [1.0, 2.0, 3.0]  # Expired if current_time is 12.0 and window_seconds is 10.0
    current_time = 12.0
    limit = 2
    window_seconds = 10.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert new_timestamps == [12.0]

def test_empty_timestamps_always_allows():
    """Test that empty timestamps always allow the request and append current_time."""
    timestamps = []
    current_time = 1.0
    limit = 1
    window_seconds = 1.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert new_timestamps == [1.0]

def test_zero_window_seconds_rejects_all_but_current():
    """Test that with window_seconds=0, only the current_time is considered."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 1
    window_seconds = 0.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert new_timestamps == [4.0]

def test_limit_zero_rejects_all_requests():
    """Test that with limit=0, all requests are rejected."""
    timestamps = []
    current_time = 1.0
    limit = 0
    window_seconds = 1.0
    allowed, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert new_timestamps == []