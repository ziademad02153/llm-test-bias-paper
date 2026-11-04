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
    """Test request is denied when tokens are insufficient."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.5,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is False
    assert remaining == 1.5  # 0.5 + (1*1) = 1.5 (request denied)
    assert new_last_refill == 1.0

def test_full_refill_capacity_respected():
    """Test tokens never exceed capacity after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 5.0  # 2 + (10*1) = 12, capped at 5
    assert new_last_refill == 1.0

def test_multiple_refill_periods_elapsed():
    """Test correct refill when multiple periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=5.0
    )
    assert allowed is True
    assert remaining == 2.0  # 0 + (2*3.5) - 5 = 2.0
    assert new_last_refill == 3.5

def test_zero_refill_rate_no_tokens_added():
    """Test no tokens are added if refill_rate is zero."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=5.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 1.0  # 3 + (0*5) - 2 = 1.0
    assert new_last_refill == 5.0

def test_request_time_before_last_refill_raises_error():
    """Test invalid request_time (before last_refill_time) raises error."""
    try:
        evaluate_token_bucket(
            capacity=10.0,
            refill_rate=1.0,
            refill_period=1.0,
            current