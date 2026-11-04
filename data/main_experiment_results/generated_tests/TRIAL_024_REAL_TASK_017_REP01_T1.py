# Test standard input with allowed rate
def test_allowed_rate():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [2.0, 3.0, 4.0]

# Test standard input with rate limit exceeded
def test_exceeded_rate():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

# Test edge case with empty input
def test_empty_input():
    timestamps = []
    current_time = 1.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [1.0]

# Test edge case with expired timestamps
def test_expired_timestamps():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 6.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [6.0]

# Test edge case with zero limit
def test_zero_limit():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 0
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == [1.0, 2.0, 3.0]

# Test edge case with negative limit
def test_negative_limit():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = -1
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == [1.0, 2.0, 3.0]