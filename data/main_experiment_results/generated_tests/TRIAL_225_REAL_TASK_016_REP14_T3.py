def test_standard_refill_and_allow():
    # Test standard refill and allow behavior
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=2.0, cost=3.0
    )
    assert allowed is True
    assert remaining == 6.0
    assert new_last_refill == 2.0

def test_deny_request_due_to_insufficient_tokens():
    # Test deny behavior when tokens are insufficient
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=2.0, last_refill_time=0.0, request_time=1.0, cost=3.0
    )
    assert allowed is False
    assert remaining == 2.0
    assert new_last_refill == 1.0

def test_refill_up_to_capacity():
    # Test that tokens do not exceed capacity after refill
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=5.0, refill_period=1.0, 
        current_tokens=8.0, last_refill_time=0.0, request_time=1.0
    )
    assert allowed is True
    assert remaining == 10.0
    assert new_last_refill == 1.0

def test_no_refill_if_request_time_before_last_refill():
    # Test no refill if request time is before last refill time
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=2.0, request_time=1.0
    )
    assert allowed is True
    assert remaining == 4.0
    assert new_last_refill == 2.0

def test_edge_case_zero_capacity():
    # Test edge case where capacity is zero
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=0.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=0.0, last_refill_time=0.0, request_time=1.0
    )
    assert allowed is False
    assert remaining == 0.0
    assert new_last_refill == 1.0

def test_edge_case_zero_refill_rate():
    # Test edge case where refill rate is zero
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=0.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0
    )
    assert allowed is True
    assert remaining == 4.0
    assert new_last_refill == 1.0