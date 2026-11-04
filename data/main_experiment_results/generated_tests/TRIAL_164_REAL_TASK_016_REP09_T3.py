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
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1.0 + 1.0 (refill)
    assert new_last_refill == 1.0

def test_refill_multiple_periods():
    """Test token refill over multiple periods, ensuring tokens don't exceed capacity."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=3.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 10.0  # 5.0 + 3.0 (refill) capped at 10.0
    assert new_last_refill == 3.0

def test_no_refill_if_no_time_passed():
    """Test that no tokens are refilled if no time has passed since last refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=1.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5.0 - 1.0 (no refill)
    assert new_last_refill == 1.0

def test_edge_case_zero_capacity():
    """Test behavior when capacity is zero (should always deny requests)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=0.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is False
    assert remaining == 0.0
    assert new_last_refill == 1.0

def test_edge_case_large_cost():
    """Test behavior when cost exceeds capacity (should always deny)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill