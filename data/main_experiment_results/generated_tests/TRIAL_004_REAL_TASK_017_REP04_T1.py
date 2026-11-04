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

# Test edge case: limit exceeded
def test_limit_exceeded():
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]

# Test edge case: window size exceeded
def test_window_size_exceeded():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 1.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [4.0]

# Test edge case: limit is 0
def test_limit_zero():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 0
    window_seconds = 3.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == False
    assert updated_timestamps == [1.0, 2.0, 3.0]

# Test edge case: window size is 0
def test_window_size_zero():
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 0.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
    assert allowed == True
    assert updated_timestamps == [4.0]

test_standard_input()
test_empty_input()
test_limit_exceeded()
test_window_size_exceeded()
test_limit_zero()
test_window_size_zero()