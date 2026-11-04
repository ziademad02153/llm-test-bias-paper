Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function:

```python
def test_normal_request_allowed():
    """Test normal case where request is allowed with sufficient tokens."""
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
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.5,
        last_refill_time=0.0,
        request_time=0.5,
        cost=1.0
    )
    assert allowed is False
    assert remaining == 1.0  # 0.5 + (0.5/1)*1 = 1.0 (but cost is 1.0, so not enough)
    assert new_last_refill == 0.5

def test_full_refill_after_long_period():
    """Test that tokens are capped at capacity after long refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=10.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # min(5, 0 + (10/1)*1) - 1 = 4
    assert new_last_refill == 10.0

def test_fractional_refill_and_cost():
    """Test with fractional refill rates and costs."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=1.0,
        refill_rate=0.5,
        refill_period=1.0,
        current_tokens=0.2,
        last_refill_time=0.0,
        request_time=0.4,
        cost=0.3
    )
    assert allowed is True
    assert abs(remaining - 0.4) < 1e-9  # 0.2 + (0.4/1)*0.5 - 0.3 = 0.4
    assert new_last_refill == 0.4

def test_zero_capacity_always_denies():
    """Test that with zero capacity, all requests are denied."""
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

def test_multiple_refill_periods():
    """Test that multiple refill periods calculate correctly."""
    allowed, remaining, new_last_refill = evaluate_token_bucket