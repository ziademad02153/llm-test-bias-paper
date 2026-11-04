Here's a comprehensive set of unit tests for the `evaluate_token_bucket` function:

```python
def test_normal_request_allowed():
    """Test a normal request that should be allowed."""
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
    assert remaining == 8.0  # 5 + (1/1)*5 - 2 = 8
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
    assert remaining == 2.0  # 1 + (0.5/1)*2 = 2 (not enough for cost=3)
    assert new_last_refill == 0.5

def test_token_refill_up_to_capacity():
    """Test that tokens don't exceed capacity when refilling."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=4.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # min(5, 4 + 10) - 1 = 5 (capped at capacity)
    assert new_last_refill == 1.0

def test_zero_refill_period_handling():
    """Test behavior when refill_period is zero (should handle division)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=0.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    # With refill_period=0, refill_amount becomes infinite, so tokens should be at capacity
    assert allowed is True
    assert remaining == 10.0  # min(capacity, 5 + inf) - 1 = 10
    assert new_last_refill == 1.0

def test_multiple_refill_periods_elapsed():
    """Test when multiple refill periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 6.0  # min(10, 0 + (3.5/1)*2) - 1 = 6
    assert new_last_refill == 3.5

def test_fractional_token_handling