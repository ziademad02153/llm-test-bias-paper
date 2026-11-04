def test_empty_timestamps_allows_request():
    """Test that an empty list of timestamps allows the request and appends current_time."""
    allowed, updated_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed and appends current_time."""
    timestamps = [90.0, 95.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert updated_timestamps == [90.0, 95.0, 97.0, 100.0]

def test_exceeds_limit_denies_request():
    """Test that a request exceeding the limit is denied and does not append current_time."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert updated_timestamps == [90.0, 95.0, 97.0, 98.0, 99.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    timestamps = [90.0, 95.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 105.0, 5, 5.0)
    assert allowed is True
    assert updated_timestamps == [105.0]

def test_boundary_case_at_window_edge():
    """Test the boundary case where a timestamp is exactly at the window edge."""
    timestamps = [95.0, 100.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 105.0, 2, 5.0)
    assert allowed is True
    assert updated_timestamps == [100.0, 105.0]