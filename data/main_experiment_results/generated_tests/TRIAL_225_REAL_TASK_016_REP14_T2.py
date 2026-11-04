def test_standard_request_allowed():
    """Test standard case where request is allowed and tokens are consumed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 8.0  # 5 + (5*1/1) = 10, then 10 - 2 = 8
    assert new_last_refill == 1.0

def test_request_denied_due_to_insufficient_tokens():
    """Test case where request is denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=5.0
    )
    assert allowed is False
    assert remaining == 3.5  # 1 + (5*0.5/1) = 3.5
    assert new_last_refill == 0.5

def test_refill_capped_at_capacity():
    """Test that tokens are refilled but capped at bucket capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=9.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 10.0  # 9 + 5 = 14, capped at 10, then 10 - 1 = 9
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test case where refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is True
    assert remaining == 2.0  # 5 + 0 = 5, then 5 - 3 = 2
    assert new_last_refill == 1.0

def test_partial_refill_period():
    """Test refill calculation with a partial refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=2.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is True
    assert remaining == 4.5  # 2 + (5*1/2) = 4.5, then 4.5 - 3 = 1.5
    assert new_last_refill == 1.0

def test_cost_greater_than_capacity():
    """Test case where cost exceeds bucket capacity (always denied)."""
    allowed, remaining, new_last_refill = evaluate_token