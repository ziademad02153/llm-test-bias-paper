def test_empty_timestamps():
    timestamps = []
    current_time = 10.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [current_time]

def test_all_timestamps_within_window():
    timestamps = [5.0, 6.0, 7.0]
    current_time = 8.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == timestamps

def test_some_timestamps_expired():
    timestamps = [1.0, 2.0, 9.0]
    current_time = 10.0
    limit = 2
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [9.0, current_time]

def test_all_timestamps_expired():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 10.0
    limit = 2
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [current_time]

def test_limit_exactly_reached():
    timestamps = [5.0, 6.0, 7.0]
    current_time = 8.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == timestamps

def test_limit_not_reached():
    timestamps = [5.0, 6.0]
    current_time = 7.0
    limit = 3
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [5.0, 6.0, current_time]