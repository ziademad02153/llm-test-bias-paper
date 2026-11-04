def test_empty_timestamps_allows_request():
    """Test that an empty list of timestamps allows the request and appends the current time."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed and the timestamp is appended."""
    timestamps = [90.0, 95.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 4
    assert 100.0 in updated_timestamps

def test_exceeds_limit_rejects_request():
    """Test that a request exceeding the limit is rejected and the timestamp is not appended."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [90.0, 95.0, 100.0]  # 90.0 is expired if current_time is 101.0 and window is 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 101.0, 2, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 2
    assert 90.0 not in updated_timestamps
    assert 101.0 in updated_timestamps

def test_exact_limit_behavior():
    """Test the behavior when the number of timestamps is exactly at the limit."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps