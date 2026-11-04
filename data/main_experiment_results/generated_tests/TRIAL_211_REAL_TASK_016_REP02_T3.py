def test_standard_request_allowed():
    """Test a standard request that should be allowed with sufficient tokens."""
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
    assert remaining == 4.0  # 5.0 - 2.0 + 1.0 (refill)
    assert new_last_refill == 1.0

def test_request_denied_due_to_insufficient_tokens():
    """Test a request that should be denied due to insufficient tokens."""
    allowed, remaining, new_last_refiff = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1.0 + 1.0 (refill), but request denied
    assert new_last_refiff == 1.0

def test_multiple_refill_periods_elapsed():
    """Test token refill when multiple refill periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.5  # 2.0 + 3.0 (refill) - 1.0 (cost) + 0.5 (partial refill)
    assert new_last_refill == 3.5

def test_capacity_not_exceeded():
    """Test that tokens never exceed capacity even after long idle periods."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=10.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # Capped at capacity (3.0 + 10.0 refill would exceed 5.0)
    assert new_last_refill == 10.0

def test_zero_cost_request():
    """Test a request with zero cost (should always be allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 1.0  # 0.0 + 1.0 (refill) - 0.0 (cost)
    assert new_last_refill == 1.0