def test_empty_timestamps_allows_request():
    """Test that an empty timestamps list allows the request and appends current_time."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 5, 60.0)
    assert allowed is True
    assert timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that a request within the limit is allowed and appends current_time."""
    allowed, timestamps = check_sliding_window_rate_limit([90.0, 95.0], 100.0, 3, 60.0)
    assert allowed is True
    assert timestamps == [90.0, 95.0, 100.0]

def test_exceeds_limit_denies_request():
    """Test that a request exceeding the limit is denied and does not append current_time."""
    allowed, timestamps = check_sliding_window_rate_limit([90.0, 95.0, 100.0], 101.0, 3, 60.0)
    assert allowed is False
    assert timestamps == [90.0, 95.0, 100.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking the limit."""
    allowed, timestamps = check_sliding_window_rate_limit([40.0, 90.0, 95.0], 100.0, 3, 60.0)
    assert allowed is True
    assert timestamps == [90.0, 95.0, 100.0]

def test_zero_limit_denies_all_requests():
    """Test that a zero limit denies all requests."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 0, 60.0)
    assert allowed is False
    assert timestamps == []

def test_window_size_zero_allows_all_requests():
    """Test that a zero window size allows all requests (edge case)."""
    allowed, timestamps = check_sliding_window_rate_limit([90.0, 95.0], 100.0, 3, 0.0)
    assert allowed is True
    assert timestamps == [90.0, 95.0, 100.0]