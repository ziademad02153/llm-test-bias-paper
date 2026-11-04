def test_empty_timestamps_allowed():
    """Test that an empty list of timestamps allows the current time."""
    allowed, timestamps = check_sliding_window_rate_limit([], 100.0, 5, 10.0)
    assert allowed is True
    assert timestamps == [100.0]

def test_within_limit_allowed():
    """Test that timestamps within the limit are allowed."""
    timestamps = [95.0, 96.0, 97.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is True
    assert len(updated_timestamps) == 4
    assert 100.0 in updated_timestamps

def test_exceeds_limit_denied():
    """Test that exceeding the limit denies the current time."""
    timestamps = [95.0, 96.0, 97.0, 98.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 10.0)
    assert allowed is False
    assert len(updated_timestamps) == 5
    assert 100.0 not in updated_timestamps

def test_evict_expired_timestamps():
    """Test that expired timestamps are evicted."""
    timestamps = [90.0, 95.0, 99.0]
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 5, 5.0)
    assert allowed is True
    assert len(updated_timestamps) == 2
    assert 90.0 not in updated_timestamps
    assert 100.0 in updated_timestamps

def test_zero_limit_denies_all():
    """Test that a zero limit denies all requests."""
    timestamps = []
    allowed, updated_timestamps = check_sliding_window_rate_limit(timestamps, 100.0, 0, 10.0)
    assert allowed is False
    assert updated_timestamps == []