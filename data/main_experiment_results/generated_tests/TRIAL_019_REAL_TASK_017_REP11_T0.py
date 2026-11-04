def test_empty_timestamps():
    assert check_sliding_window_rate_limit([], 10.0, 5, 60.0) == (True, [10.0])

def test_rate_limit_not_exceeded():
    timestamps = [1.0, 2.0, 3.0]
    assert check_sliding_window_rate_limit(timestamps, 4.0, 5, 60.0) == (True, [1.0, 2.0, 3.0, 4.0])

def test_rate_limit_exceeded():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert check_sliding_window_rate_limit(timestamps, 6.0, 5, 60.0) == (False, [1.0, 2.0, 3.0, 4.0, 5.0])

def test_expired_timestamps_evicted():
    timestamps = [1.0, 61.0, 62.0]
    assert check_sliding_window_rate_limit(timestamps, 120.0, 5, 60.0) == (True, [61.0, 62.0, 120.0])

def test_zero_window_seconds():
    timestamps = [1.0, 2.0, 3.0]
    assert check_sliding_window_rate_limit(timestamps, 4.0, 5, 0.0) == (True, [4.0])

def test_zero_limit():
    timestamps = [1.0, 2.0, 3.0]
    assert check_sliding_window_rate_limit(timestamps, 4.0, 0, 60.0) == (False, [1.0, 2.0, 3.0])