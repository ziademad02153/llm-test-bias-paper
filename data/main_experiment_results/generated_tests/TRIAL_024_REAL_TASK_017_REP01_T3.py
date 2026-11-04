# Test case 1: Standard input with timestamps within the window
timestamps = [100.0, 101.0, 102.0]
current_time = 103.0
limit = 3
window_seconds = 5.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is True
assert updated_timestamps == [100.0, 101.0, 102.0, 103.0]

# Test case 2: Timestamps partially expired, current_time appended
timestamps = [100.0, 101.0, 102.0]
current_time = 106.0
limit = 3
window_seconds = 5.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is True
assert updated_timestamps == [101.0, 102.0, 106.0]

# Test case 3: Rate limit exceeded
timestamps = [100.0, 101.0, 102.0, 103.0]
current_time = 104.0
limit = 3
window_seconds = 5.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is False
assert updated_timestamps == [100.0, 101.0, 102.0, 103.0]

# Test case 4: Empty timestamps list, current_time appended
timestamps = []
current_time = 100.0
limit = 3
window_seconds = 5.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is True
assert updated_timestamps == [100.0]

# Test case 5: All timestamps expired, current_time appended
timestamps = [90.0, 91.0, 92.0]
current_time = 100.0
limit = 3
window_seconds = 5.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is True
assert updated_timestamps == [100.0]

# Test case 6: Edge case with zero window_seconds
timestamps = [100.0, 101.0, 102.0]
current_time = 103.0
limit = 3
window_seconds = 0.0
result, updated_timestamps = check_sliding_window_rate_limit(timestamps, current_time, limit, window_seconds)
assert result is False
assert updated_timestamps == [100.0, 101.0, 102.0]