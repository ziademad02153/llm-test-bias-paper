def test_standard_input():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [2.0, 3.0, 4.0]

def test_rate_limit_exceeded():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

def test_empty_timestamps():
    timestamps = []
    current_time = 1.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [1.0]

def test_expired_timestamps():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 1.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed
    assert updated_timestamps == [4.0]

def test_zero_limit():
    timestamps = []
    current_time = 1.0
    limit = 0
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == []

def test_negative_limit():
    timestamps = []
    current_time = 1.0
    limit = -1
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert not allowed
    assert updated_timestamps == []