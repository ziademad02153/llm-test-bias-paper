def test_empty_timestamps():
    """Test with empty timestamps list."""
    timestamps = []
    current_time = 10.0
    limit = 5
    window_seconds = 60.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [current_time]

def test_allowed_request():
    """Test with allowed request."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 10.0
    limit = 5
    window_seconds = 60.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [current_time]

def test_rate_limit_exceeded():
    """Test with rate limit exceeded."""
    timestamps = [10.0, 10.1, 10.2, 10.3, 10.4]
    current_time = 10.5
    limit = 5
    window_seconds = 1.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == timestamps

def test_expired_timestamps():
    """Test with expired timestamps."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 10.0
    limit = 5
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [current_time]

def test_zero_limit():
    """Test with zero limit."""
    timestamps = []
    current_time = 10.0
    limit = 0
    window_seconds = 60.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == []

def test_negative_limit():
    """Test with negative limit."""
    timestamps = []
    current_time = 10.0
    limit = -1
    window_seconds = 60.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == []