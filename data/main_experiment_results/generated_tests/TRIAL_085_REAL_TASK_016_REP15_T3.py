Here's a comprehensive test suite for the `evaluate_token_bucket` function based on its specification:

```python
def test_standard_request_allowed():
    """Test standard case where request is allowed with sufficient tokens"""
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
    """Test request is denied when not enough tokens available"""
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
    """Test proper token refill when multiple periods have elapsed"""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=1.0,
        current_tokens=0.0,
        last_refill_time=0.0,
        request_time=3.5,
        cost=0.0
    )
    assert allowed is True
    assert remaining == 3.0  # 3 periods elapsed, but capped at capacity
    assert new_last_refill == 3.5

def test_tokens_never_exceed_capacity():
    """Test that tokens never exceed bucket capacity"""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=5.0,
        refill_rate=2.0,
        refill_period=1.0,
        current_tokens=4.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=0.0
    )
    assert remaining == 5.0  # Should cap at capacity (4 + 2 = 6 → capped to 5)
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    """Test behavior with zero refill rate (no tokens ever added)"""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=0.0,
        refill_period=1.0,
        current_tokens=5.0,
        last_refill_time=0.0,
        request_time=10.0,
        cost=1.0
    )
    assert allowed is True
    assert remaining == 4.0  # No refill happens
    assert new_last_refill == 10.0

def test_fractional_refill():
    """Test fractional token refill calculation"""
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0,
        refill_rate=1.0,
        refill_period=2.0,  # 0.5 tokens per second
        current_tokens=1.0,
        last_refill_time=0.0,
        request_time=1.0,
        cost=1.25
    )
    assert allowed is False  #