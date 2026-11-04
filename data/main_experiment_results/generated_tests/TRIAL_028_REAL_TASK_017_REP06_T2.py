def test_empty_timestamps_allows_request():
    """Test that an empty list of timestamps allows the request."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed."""
    timestamps = [90.0, 95.0, 98.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 4
    assert 100.0 in updated_timestamps

def test_exceeds_limit_rejects_request():
    """Test that a request exceeding the limit is rejected."""
    timestamps = [90.0, 95.0, 98.0, 99.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 101.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5  # No new timestamp added

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted."""
    timestamps = [90.0, 95.0, 98.0, 99.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 105.0, 5, 5.0)
    assert allowed is True  # Only 100.0 is within the 5-second window
    assert updated_timestamps == [100.0, 105.0]

def test_boundary_case_exact_window():
    """Test the boundary case where a timestamp is exactly at the window edge."""
    timestamps = [90.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 2, 10.0)
    assert allowed is False  # 90.0 is exactly at the 10-second window edge (100-90=10)
    assert len(updated_timestamps) == 1  # 90.0 is evicted (strictly less than window)