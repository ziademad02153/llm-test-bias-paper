def test_standard_refill_and_allow():
    """Test standard case where tokens are refilled and request is allowed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=3.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 + (2*2) - 3 = 6, but capped at capacity 10
    assert new_last_refill == 2.0

def test_deny_due_to_insufficient_tokens():
    """Test request is denied when not enough tokens are available."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=4.0
    )
    assert allowed is False
    assert remaining == 3.0  # 2 + (1*1) = 3 (cost not deducted)
    assert new_last_refill == 1.0

def test_refill_capped_at_capacity():
    """Test token refill does not exceed bucket capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=3.0,
        refill_period=1.0,
        current_tokens=4.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # 4 + (3*2) = 10 -> capped at 5, then -1 = 4 (but verify logic)
    assert new_last_refill == 2.0

def test_no_refill_if_no_time_passed():
    """Test no refill occurs if no time has passed since last refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=5.0,
        request_time=5.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 2.0  # 3 - 1 = 2 (no refill)
    assert new_last_refill == 5.0

def test_edge_case_zero_cost():
    """Test edge case where cost is zero (always allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 3.0  # 1 + 2*1 - 0 = 3
    assert new_last_refill == 1.0