def test_standard_input():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 3
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [2.0, 3.0, 4.0]

def test_rate_limit_exceeded():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 2
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == [1.0, 2.0, 3.0]

def test_empty_input():
    timestamps = []
    current_time = 1.0
    limit = 3
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [1.0]

def test_expired_timestamps():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.1
    limit = 3
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [3.0, 4.1]

def test_zero_limit():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 0
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == [1.0, 2.0, 3.0]

def test_negative_window_seconds():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 3
    window_seconds = -1.0
    try:
        check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
        assert False, "Expected an exception for negative window_seconds"
    except Exception:
        assert True