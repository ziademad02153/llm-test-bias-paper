def test_empty_timestamps():
    timestamps = []
    current_time = 10.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [current_time]

def test_within_limit():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0]

def test_exceed_limit():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is False
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

def test_evict_expired_timestamps():
    timestamps = [1.0, 2.0, 3.0, 11.0]
    current_time = 12.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [11.0, 12.0]

def test_edge_case_exact_window():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 11.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0, 11.0]

def test_edge_case_empty_after_eviction():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 12.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed is True
    assert updated_timestamps == [12.0]