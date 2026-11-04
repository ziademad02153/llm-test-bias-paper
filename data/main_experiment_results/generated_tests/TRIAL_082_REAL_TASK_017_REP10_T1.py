# Test standard input
def test_standard_input():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [2.0, 3.0, 4.0]

# Test edge case: empty input
def test_empty_input():
    timestamps = []
    current_time = 1.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [1.0]

# Test edge case: limit reached
def test_limit_reached():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

# Test edge case: expired timestamps
def test_expired_timestamps():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 6.0
    limit = 5
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [6.0]

# Test edge case: zero limit
def test_zero_limit():
    timestamps = []
    current_time = 1.0
    limit = 0
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == []

test_standard_input()
test_empty_input()
test_limit_reached()
test_expired_timestamps()
test_zero_limit()