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
    assert remaining == 5.0  # 5 + (2*1) - 2 = 5
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test case where request is denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (1*1) = 2 (request denied)
    assert new_last_refill == 1.0

def test_full_capacity_no_refill_needed():
    """Test case where bucket is full and no refill is needed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=10.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # 10 - 1 = 9 (no refill yet)
    assert new_last_refill == 0.0  # No refill happened

def test_multiple_refill_periods_elapsed():
    """Test case where multiple refill periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.0,
        cost=5.0
    )
    assert allowed is True
    assert remaining == 1.0  # 0 + (2*3) - 5 = 1 (capped at capacity)
    assert new_last_refill == 3.0

def test_zero_refill_rate():
    """Test case with zero refill rate (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=2.0,
        cost=4.0
    )
    assert allowed is True
    assert remaining == 1.0  # 5 + 0 - 4 = 1
    assert new_last_refill == 0.0  # No refill happened (rate=0)