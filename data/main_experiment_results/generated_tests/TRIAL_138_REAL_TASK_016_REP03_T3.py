Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function based on its specification:

```python
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
    assert remaining == 4.0  # 5.0 + (1.0 * 1.0) - 2.0 = 4.0
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test request is denied when not enough tokens available."""
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
    assert remaining == 2.0  # 1.0 + (1.0 * 1.0) = 2.0 (request denied)
    assert new_last_refill == 1.0

def test_full_refill_after_long_period():
    """Test tokens are capped at capacity after long refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=20.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # min(0 + (1.0 * 20), 10) - 1.0 = 9.0
    assert new_last_refill == 20.0

def test_multiple_refill_periods():
    """Test proper token calculation when multiple refill periods have passed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # min(0 + (2.0 * 3), 5) - 1.0 = 5.0 - 1.0 = 4.0
    assert new_last_refill == 3.0

def test_zero_cost_request():
    """Test behavior when cost is zero (always allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 2.0  # 1.0 + (1.0 * 1.0) - 0.0 = 2.0
    assert new_last_refill == 1.