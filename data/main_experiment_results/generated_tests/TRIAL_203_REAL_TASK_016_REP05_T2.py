def test_standard_case():
    # Test standard case where tokens are refilled and request is allowed
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=3.0
    )
    assert allowed == True
    assert remaining == 4.0
    assert new_last_refill == 1.0

def test_no_refill_needed():
    # Test case where no refill is needed and request is allowed
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=8.0, last_refill_time=0.0, request_time=0.5, cost=3.0
    )
    assert allowed == True
    assert remaining == 5.0
    assert new_last_refill == 0.5

def test_request_denied():
    # Test case where request is denied due to insufficient tokens
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=1.0, last_refill_time=0.0, request_time=1.0, cost=3.0
    )
    assert allowed == False
    assert remaining == 3.0
    assert new_last_refill == 1.0

def test_capacity_exceeded():
    # Test case where refill exceeds capacity
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=20.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=3.0
    )
    assert allowed == True
    assert remaining == 7.0
    assert new_last_refill == 1.0

def test_zero_cost():
    # Test case where cost is zero
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=0.0
    )
    assert allowed == True
    assert remaining == 7.0
    assert new_last_refill == 1.0

def test_negative_elapsed_time():
    # Test case where elapsed time is negative (invalid scenario)
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=1.0, request_time=0.0, cost=3.0
    )
    assert allowed == False
    assert remaining == 5.0
    assert new_last_refill == 0.0