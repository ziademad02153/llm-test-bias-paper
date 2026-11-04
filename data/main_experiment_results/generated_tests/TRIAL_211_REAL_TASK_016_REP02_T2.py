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
    assert remaining == 4.0  # 5 + (1/1)*2 = 7, then 7 - 3 = 4
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test case where request is denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=5.0
    )
    assert allowed is False
    assert remaining == 3.0  # 2 + (1/1)*1 = 3, which is < 5
    assert new_last_refill == 1.0

def test_refill_capped_at_capacity():
    """Test that tokens are refilled but capped at bucket capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # 0 + (1/1)*10 = 10, capped to 5, then 5 - 1 = 4
    assert new_last_refill == 1.0

def test_multiple_refill_periods_elapsed():
    """Test refill when multiple refill periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 6.0  # 0 + (3.5/1)*2 = 7, then 7 - 1 = 6
    assert new_last_refill == 3.5

def test_zero_cost_request():
    """Test edge case where cost is zero (always allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 2.0  # 0 + (1/1)*2 = 2, then 2 - 0 = 2
    assert new_last_refill == 1.0

def test_no_time_elapsed():
    """Test case where no time has elapsed since last refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket