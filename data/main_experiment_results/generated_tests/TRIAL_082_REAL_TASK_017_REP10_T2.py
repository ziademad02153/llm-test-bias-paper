def test_empty_timestamps_allows_request():
    """Test that an empty list of timestamps allows the request."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed."""
    timestamps = [90.0, 95.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [90.0, 95.0, 97.0, 100.0]

def test_exceeds_limit_denies_request():
    """Test that a request exceeding the limit is denied."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == [90.0, 95.0, 97.0, 98.0, 99.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted."""
    timestamps = [80.0, 90.0, 95.0, 97.0]  # 80.0 is expired (100 - 80 = 20 > 10)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [90.0, 95.0, 97.0, 100.0]

def test_exact_limit_denies_request():
    """Test that a request at the exact limit is denied."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == [90.0, 95.0, 97.0, 98.0, 99.0]

def test_all_expired_timestamps_allows_request():
    """Test that all expired timestamps are evicted, allowing the request."""
    timestamps = [80.0, 85.0, 89.0]  # All expired (100 - 89 = 11 > 10)
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]