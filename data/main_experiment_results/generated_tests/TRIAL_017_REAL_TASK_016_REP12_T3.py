Here's a comprehensive suite of unit tests for the `evaluate_token_bucket` function based on its specification:

```python
def test_standard_request_allowed():
    """Test a standard request that should be allowed with sufficient tokens."""
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

def test_request_denied_due_to_insufficient_tokens():
    """Test a request that should be denied due to insufficient tokens."""
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
    assert remaining == 1.5  # 1 + (1*0.5) = 1.5 (not enough for cost=2)
    assert new_last_refill == 0.5

def test_refill_up_to_capacity():
    """Test that tokens never exceed bucket capacity after refill."""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=10.0,  # High refill rate to test capacity limit
        refill_period=1.0,
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0  # No cost to test just refill
    )
    assert allowed is True
    assert remaining == 5.0  # Should cap at capacity
    assert new_last_refill == 1.0

def test_multiple_refill_periods():
    """Test token refill over multiple periods."""
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
    assert remaining == 2.0  # 0 + (2*3.5) - 5 = 2
    assert new_last_refill == 3.5

def test_zero_cost_request():
    """Test a request with zero cost (should always be allowed)."""
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
    assert remaining == 0.5  # 0 + (1*0.5) - 0 = 0.5
    assert new_last_refill == 0.5

def test_immediate_request_after_refill():
    """Test a request made immediately after last refill (no time elapsed)."""
    allowed, remaining, new_last_ref