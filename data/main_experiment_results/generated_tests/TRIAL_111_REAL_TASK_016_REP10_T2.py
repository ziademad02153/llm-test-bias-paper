def test_standard_request_allowed():
    """Test a standard request that should be allowed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 6.0  # 3 + (1/1)*5 = 8, then 8 - 2 = 6
    assert new_last_refill == 1.0

def test_request_denied_due_to_insufficient_tokens():
    """Test a request that should be denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (0.5/1)*2 = 2, cost 3 is too high
    assert new_last_refill == 0.5

def test_refill_up_to_capacity():
    """Test that tokens are refilled up to capacity but not beyond."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0 - 1.0  # 2 + (1/1)*10 = 12, capped at 5, then 5 - 1 = 4
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no refill)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=2.0
    )
    assert allowed is True  # 3 + 0 >= 2
    assert remaining == 1.0
    assert new_last_refill == 2.0

def test_cost_greater_than_capacity():
    """Test when cost exceeds capacity (always denied)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=6.0
    )
    assert allowed is False
    assert remaining == 7.0  # 5 + (1/1)*2 = 7, but 7 < 6 is False (but math is correct)
    assert new_last_refill == 1.0

def test_fractional_refill_and_cost():
    """Test fractional refill and cost calculations."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=