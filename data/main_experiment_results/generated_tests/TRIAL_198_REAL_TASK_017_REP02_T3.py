def test_below_limit_allows_and_appends():
    """Test that a request below the limit is allowed and current_time is appended."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 10.0
    allowed, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert allowed is True
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0]


def test_above_limit_rejects_and_evicts():
    """Test that a request above the limit is rejected and old timestamps are evicted."""
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 5.0  # Only timestamps >= 1.0 (6.0 - 5.0) are kept
    allowed, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert allowed is False
    assert new_timestamps == [2.0, 3.0, 4.0, 5.0]  # 1.0 is evicted


def test_empty_timestamps_allows():
    """Test that an empty timestamps list allows the request and appends current_time."""
    timestamps = []
    current_time = 1.0
    limit = 1
    window_seconds = 1.0
    allowed, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert allowed is True
    assert new_timestamps == [1.0]


def test_exact_limit_rejects():
    """Test that a request at the exact limit is rejected."""
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0  # No eviction, but limit is hit
    allowed, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert allowed is False
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]  # No eviction, but no append


def test_evicts_all_expired_timestamps():
    """Test that all expired timestamps are evicted."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 11.0
    limit = 5
    window_seconds = 5.0  # Only timestamps >= 6.0 (11.0 - 5.0) are kept
    allowed, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert allowed is True
    assert new_timestamps == [11.0]  # All old timestamps are evicted