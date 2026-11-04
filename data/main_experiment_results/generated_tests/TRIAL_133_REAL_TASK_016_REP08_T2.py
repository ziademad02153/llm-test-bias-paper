def test_standard_request_allowed():
    """Test a standard request that should be allowed with correct token update."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 6.0  # 3 + (2/1)*5 - 2 = 6
    assert new_last_refill == 2.0

def test_request_denied_due_to_insufficient_tokens():
    """Test a request that should be denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=5.0
    )
    assert allowed is False
    assert remaining == 3.0  # 1 + (1/1)*2 = 3 (cost not subtracted)
    assert new_last_refill == 1.0

def test_refill_up_to_capacity():
    """Test that tokens are refilled up to capacity but not beyond."""
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
    assert remaining == 4.0  # min(5, 0 + 10) - 1 = 4
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=5.0,
        cost=3.0
    )
    assert allowed is False  # 2 + 0 < 3
    assert remaining == 2.0
    assert new_last_refill == 5.0

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
    assert remaining == 7.0  # 5 + 2 = 7 (but 7 > capacity, capped at 5)
    assert new_last_refill == 1.0

def test_fractional_tokens_and_cost():
    """Test fractional tokens and cost calculations."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.5,
        refill_period=1.0,
        current_tokens=1.5,