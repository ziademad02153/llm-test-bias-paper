def test_empty_timestamps_allows_request():
    """Test that an empty list of timestamps allows the request."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed."""
    timestamps = [90.0, 95.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 4
    assert 100.0 in updated_timestamps

def test_exceeds_limit_rejects_request():
    """Test that a request exceeding the limit is rejected."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted."""
    timestamps = [90.0, 95.0, 110.0]  # 90.0 is expired if current_time is 100.0 and window is 10.0
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 2
    assert 90.0 not in updated_timestamps
    assert 100.0 in updated_timestamps

def test_exact_limit_boundary():
    """Test the boundary case where the limit is exactly reached."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]  # 5 requests (limit is 5)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_window_size_zero():
    """Test edge case where window size is zero (all timestamps are expired)."""
    timestamps = [90.0, 95.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 0.0)
    assert allowed is True
    assert len(updated_timestamps) == 1
    assert 100.0 in updated_timestamps