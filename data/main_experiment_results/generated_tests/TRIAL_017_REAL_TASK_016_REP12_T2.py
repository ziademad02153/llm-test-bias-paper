Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function:

```python
def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens."""
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
    assert remaining == 8.0  # 5 + (5*1/1) - 2 = 8
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
        cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0  # 1 + (2*0.5/1) = 2
    assert new_last_refill == 0.5

def test_token_refill_capped_at_capacity():
    """Test that token refill doesn't exceed bucket capacity."""
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
    assert remaining == 4.0  # min(5, 4 + 10) - 1 = 4
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior with zero refill rate (no new tokens added)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=2.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 1.0  # 2 + 0 - 1 = 1
    assert new_last_refill == 1.0

def test_multiple_refill_periods_elapsed():
    """Test when multiple refill periods have elapsed since last refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 7.0  # 1 + (2*3.5/1) = 8, capped at 10, then -1 = 7
    assert new_last_refill == 3.5

def test_fractional_tokens():
    """Test behavior with fractional tokens and refill amounts."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,