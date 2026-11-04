def test_empty_timestamps_allows_request():
    """Test that empty timestamps always allows the request and appends current_time."""
    result, new_timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert result is True
    assert new_timestamps == [100.0]

def test_within_limit_allows_request():
    """Test that request within limit is allowed and current_time is appended."""
    timestamps = [95.0, 97.0, 99.0]
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is True
    assert new_timestamps == [95.0, 97.0, 99.0, 100.0]

def test_exceeds_limit_rejects_request():
    """Test that request exceeding limit is rejected and timestamps are evicted."""
    timestamps = [91.0, 95.0, 97.0, 99.0, 100.0]
    current_time = 101.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False
    assert new_timestamps == [95.0, 97.0, 99.0, 100.0]

def test_evicts_expired_timestamps():
    """Test that expired timestamps are evicted before checking limit."""
    timestamps = [89.0, 91.0, 95.0, 99.0]  # 89.0 and 91.0 are expired at current_time=100.0 with window=10.0
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 2, 10.0)
    assert result is True  # After eviction, only 95.0 and 99.0 remain (under limit=2)
    assert new_timestamps == [95.0, 99.0, 100.0]

def test_exact_limit_boundary():
    """Test exact limit boundary condition (limit reached but not exceeded)."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]  # 5 requests (limit=5)
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 5, 10.0)
    assert result is False  # Exactly at limit, should reject
    assert new_timestamps == [95.0, 96.0, 97.0, 98.0, 99.0]  # No append

def test_window_edge_case():
    """Test edge case where timestamp is exactly on window boundary."""
    timestamps = [90.0]  # Exactly at current_time=100.0 with window=10.0 (should be kept)
    current_time = 100.0
    result, new_timestamps = check_sliding_window_rate_limit(timestamps, current_time, 1, 10.0)
    assert result is False  # Limit reached (1 request in window)
    assert new_timestamps == [90.0]  # No append