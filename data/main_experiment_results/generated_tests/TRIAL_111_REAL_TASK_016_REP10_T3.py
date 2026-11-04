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
    assert remaining == 4.0  # 5 + (1*1) - 2 = 4
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
    assert remaining == 2.0  # 1 + (1*1) = 2 (but request denied)
    assert new_last_refill == 1.0

def test_full_refill_after_long_period():
    """Test that tokens are capped at capacity after long refill period."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=15.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 9.0  # min(0 + (1*15), 10) - 1 = 9
    assert new_last_refill == 15.0

def test_no_refill_when_no_time_passed():
    """Test no tokens are added when no time has passed since last refill."""
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
    assert remaining == 4.0  # 5 + 0 - 1 = 4
    assert new_last_refill == 1.0

def test_edge_case_zero_capacity():
    """Test behavior with zero capacity bucket (always deny)."""
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

def test_fractional_refill_calculation():
    """Test fractional token refill calculation."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.5,
        refill_period=1.0,
        current_tokens=