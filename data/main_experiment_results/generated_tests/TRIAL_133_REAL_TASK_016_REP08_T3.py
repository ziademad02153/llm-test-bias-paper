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

def test_multiple_refill_periods_elapsed():
    """Test case where multiple refill periods have elapsed."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.5
    )
    assert allowed is True
    assert remaining == 9.5  # 3 refills (3 tokens) - 1 (cost) + 7.5 from remaining time
    assert new_last_refill == 3.5

def test_capacity_not_exceeded():
    """Test that tokens never exceed capacity after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=4.0,
        last_refill_time=0.0,
        request_time=10.0
    )
    assert allowed is True
    assert remaining == 5.0  # Should cap at capacity
    assert new_last_refill == 10.0

def test_zero_cost_request():
    """Test behavior with zero cost request (should always be allowed)."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=1.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=0.5,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 0.0
    assert new_last_refill == 0.5

def test_immediate_request_after_refill():
    """Test request immediately after last refill with no time elapsed."""
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
    assert remaining == 4.0
    assert new_last_refill ==