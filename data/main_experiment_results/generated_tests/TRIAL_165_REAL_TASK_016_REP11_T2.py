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
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (0.5/1)*2 = 2, no deduction
    assert new_last_refill == 0.5

def test_refill_up_to_capacity():
    """Test that tokens are refilled up to capacity but not beyond."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=4.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # 4 + (2/1)*2 = 8, capped at 5, then 5 - 1 = 4
    assert new_last_refill == 2.0

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

def test_large_elapsed_time_refill():
    """Test case with large elapsed time ensuring tokens don't exceed capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=20.0,
        cost=5.0
    )
    assert allowed is True
    assert remaining == 5.0  # 0 + (20/1)*1 = 20, capped at 10, then 10 - 5 = 5
    assert new_last_refill == 20.0

def test_fractional_refill_and_cost():
    """Test fractional refill rate and cost."""
    allowed, remaining, new_last_refill = evaluate_token_bucket