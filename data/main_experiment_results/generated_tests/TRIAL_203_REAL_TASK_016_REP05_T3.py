def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
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
    assert remaining == 3.0
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
        cost=2.0
    )
    assert allowed is False
    assert remaining == 1.0
    assert new_last_refill == 1.0

def test_full_refill_after_period():
    """Test tokens are fully refilled after refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # 10 refilled - 1 cost
    assert new_last_refill == 1.0

def test_partial_refill_before_period():
    """Test partial token refill when elapsed time is less than refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=0.5
    )
    assert allowed is True
    assert remaining == 4.0  # 5 refilled - 1 cost
    assert new_last_refill == 0.5

def test_capacity_not_exceeded():
    """Test that tokens never exceed bucket capacity after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=20.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # capped at 10 - 1 cost
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior when refill_rate is zero (no tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0
    )
    assert allowed is True  # enough initial tokens
    assert remaining == 0.0
    assert new_last_refill == 1.0