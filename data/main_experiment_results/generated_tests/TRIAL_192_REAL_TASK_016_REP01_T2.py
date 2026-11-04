def test_standard_request_allowed():
    """Test a standard request that should be allowed with correct token update."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 6.0  # 5 + (1/1)*2 - 1 = 6
    assert new_last_refill == 1.0

def test_request_denied_due_to_insufficient_tokens():
    """Test a request that should be denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.5,
        last_refill_time=0.0,
        request_time=0.5,
        cost=1.0
    )
    assert allowed is False
    assert remaining == 1.5  # 0.5 + (0.5/1)*2 = 1.5 (no deduction)
    assert new_last_refill == 0.5

def test_refill_up_to_capacity():
    """Test that tokens are refilled up to capacity but not beyond."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=9.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 10.0  # min(10, 9 + (2/1)*2) - 1 = 10 - 1 = 9 (but capped at 10 before deduction)
    assert new_last_refill == 2.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no refill occurs)."""
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

def test_cost_greater_than_capacity():
    """Test when cost exceeds capacity (always denied)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=10.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=11.0
    )
    assert allowed is False
    assert remaining == 12.0  # 10 + (1/1)*2 = 12 (no deduction)
    assert new_last_refill == 1.0

def test_multiple_refill_periods():
    """Test refill over multiple periods with partial refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,