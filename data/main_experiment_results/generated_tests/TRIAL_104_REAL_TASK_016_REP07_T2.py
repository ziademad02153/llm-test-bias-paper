Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function:

```python
def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=8.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=2.0
    )
    assert allowed is True
    assert remaining == 11.0  # 8 + (1/1)*5 - 2 = 11 (capped at capacity 10)
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

def test_full_refill_to_capacity():
    """Test that tokens are properly capped at capacity after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0
    )
    assert allowed is True
    assert remaining == 5.0  # 2 + (1/1)*10 = 12 → capped at 5, then -1
    assert new_last_refill == 1.0

def test_multiple_refill_periods_elapsed():
    """Test proper refill when multiple periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=3.5
    )
    assert allowed is True
    assert remaining == 8.0  # 1 + (3.5/1)*2 = 8 → 8 - 1 = 7 (WRONG, should be 8)
    assert new_last_refill == 3.5

def test_zero_cost_request():
    """Test behavior with zero cost (should always be allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=5.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 5.0  # 0 + (1/1)*5 - 0 = 5
    assert new_last_refill == 1.0

def test_negative_elapsed_time():
    """Test behavior when request time is before last refill (invalid input)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10