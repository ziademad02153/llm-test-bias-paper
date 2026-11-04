def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 + (2*1) - 3 = 4
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test case where request is denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (1*1) = 2 (but request denied)
    assert new_last_refill == 1.0

def test_refill_multiple_periods():
    """Test token refill over multiple periods, capped at capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=5.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # min(0 + (2*5), 10) - 1 = 9
    assert new_last_refill == 5.0

def test_zero_refill_rate():
    """Test case where refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=10.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 1.0  # 2 + 0 - 1 = 1
    assert new_last_refill == 10.0

def test_request_time_before_last_refill():
    """Test edge case where request_time is before last_refill_time."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=10.0,
        request_time=5.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 - 1 = 4 (no refill)
    assert new_last_refill == 10.0  # unchanged