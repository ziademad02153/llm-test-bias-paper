Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function based on its specification:

```python
def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=3.0
    )
    assert allowed is True
    assert remaining == 4.0  # 5 + (2*1) - 3 = 4
    assert new_last_refill == 1.0

def test_request_denied_insufficient_tokens():
    """Test case where request is denied due to insufficient tokens."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=2.0
    )
    assert allowed is False
    assert remaining == 1.5  # 1 + (1*0.5) = 1.5 (no deduction)
    assert new_last_refill == 0.5

def test_full_refill_after_long_period():
    """Test tokens are capped at capacity after long refill period."""
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
    assert remaining == 4.0  # min(0 + (1*10), 5) - 1 = 4
    assert new_last_refill == 10.0

def test_multiple_refill_periods():
    """Test proper token calculation across multiple refill periods."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=3.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=5.0
    )
    assert allowed is True
    # 3 + (2*3.5) = 10 (capped), then -5 = 5 remaining
    assert remaining == 5.0
    assert new_last_refill == 3.5

def test_zero_refill_rate():
    """Test behavior with zero refill rate (no new tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=10.0,
        cost=4.0
    )
    assert allowed is True
    assert remaining == 1.0  # 5 + 0 - 4 = 1
    assert new_last_refill == 10.0

def test_exact_capacity_request():
    """Test request for exactly available tokens after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=8.