def test_standard_request_allowed():
    """Test a standard request that should be allowed."""
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
    assert remaining == 2.0  # 1 + (0.5/1)*2 = 2, cost > 2
    assert new_last_refill == 0.5

def test_refill_to_capacity():
    """Test that tokens are refilled but do not exceed capacity."""
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
    assert remaining == 5.0  # 4 + (2/1)*2 = 8, capped to 5, then 5 - 1 = 4
    assert new_last_refill == 2.0

def test_zero_cost_request():
    """Test a request with zero cost (should always be allowed)."""
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

def test_elapsed_time_longer_than_refill_period():
    """Test when elapsed time is longer than refill_period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # 0 + (3/1)*2 = 6, then 6 - 1 = 5
    assert new_last_refill == 3.0

def test_request_time_before_last_refill():
    """Test edge case where request_time is before last_refill_time (invalid but should handle)."""
    allowed, remaining