def test_within_limit_returns_true_and_appends():
    """Test that current_time is appended when within limit."""
    timestamps = [1.0, 2.0, 3.0]
    current_time = 4.0
    limit = 5
    window_seconds = 10.0
    result, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert result is True
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0]


def test_exceeds_limit_returns_false_and_no_append():
    """Test that current_time is not appended when limit is exceeded."""
    timestamps = [1.0, 2.0, 3.0, 4.0, 5.0]
    current_time = 6.0
    limit = 5
    window_seconds = 10.0
    result, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert result is False
    assert new_timestamps == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_evicts_expired_timestamps():
    """Test that expired timestamps are removed before checking limit."""
    timestamps = [1.0, 2.0, 3.0]  # Expired if window_seconds=2 and current_time=4.0
    current_time = 4.0
    limit = 2
    window_seconds = 2.0
    result, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert result is True
    assert new_timestamps == [3.0, 4.0]  # 1.0 and 2.0 should be evicted


def test_empty_timestamps_allows_append():
    """Test that empty timestamps list allows append when within limit."""
    timestamps = []
    current_time = 1.0
    limit = 1
    window_seconds = 10.0
    result, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert result is True
    assert new_timestamps == [1.0]


def test_zero_limit_rejects_all():
    """Test that zero limit always rejects and never appends."""
    timestamps = []
    current_time = 1.0
    limit = 0
    window_seconds = 10.0
    result, new_timestamps = check_sliding_window_rate_limit(
        timestamps, current_time, limit, window_seconds
    )
    assert result is False
    assert new_timestamps == []