def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 5.0  # 5 + (1/1)*2 - 2 = 5
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
        cost=2.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (0.5/1)*2 = 2
    assert new_last_refill == 0.5

def test_refill_to_capacity():
    """Test that tokens are refilled but do not exceed capacity."""
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
    assert remaining == 5.0  # min(5, 2 + 10) - 1 = 5 (capped at capacity)
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=2.0
    )
    assert allowed is True  # 3 >= 2
    assert remaining == 1.0  # 3 - 2 = 1
    assert new_last_refill == 2.0

def test_fractional_refill_and_cost():
    """Test fractional refill and cost calculations."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.5,
        refill_period=3.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=0.5
    )
    assert allowed is True
    assert remaining == 3.0  # 2 + (2/3)*1.5 - 0.5 = 3
    assert new_last_refill == 2.0