def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 + (1*1) - 2 = 4
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test request is denied when not enough tokens are available."""
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
    assert remaining == 2.0  # 1 + (1*1) = 2 (request denied, tokens not spent)
    assert new_last_refill == 1.0

def test_refill_multiple_periods():
    """Test token refill over multiple periods, capped at capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=15.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 10.0  # 0 + (1*15) = 15 -> capped at 10
    assert new_last_refill == 15.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 + 0 - 1 = 4
    assert new_last_refill == 1.0

def test_request_time_before_last_refill():
    """Test edge case where request_time is before last_refill_time."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=2.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # No refill (negative elapsed time), 5 - 1 = 4
    assert new_last_refill == 2.0  # Unchanged