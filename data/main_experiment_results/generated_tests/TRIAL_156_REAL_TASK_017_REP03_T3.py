def test_within_limit_returns_true_and_appends_timestamp():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 3
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0]

def test_exceeds_limit_returns_false_and_does_not_append():
    timestamps = [1.0, 2.0, 3.0, 4.0]
    current_time = 5.0
    limit = 3
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0]

def test_evicts_expired_timestamps():
    timestamps = [1.0, 2.0, 6.0, 7.0]
    current_time = 8.0
    limit = 3
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [6.0, 7.0, 8.0]

def test_empty_timestamps_always_allows():
    timestamps = []
    current_time = 1.0
    limit = 3
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0]

def test_zero_limit_always_rejects():
    timestamps = []
    current_time = 1.0
    limit = 0
    window_seconds = 5.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert updated_timestamps == []

def test_window_seconds_zero_evicts_all_but_current():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 2
    window_seconds = 0.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [4.0]