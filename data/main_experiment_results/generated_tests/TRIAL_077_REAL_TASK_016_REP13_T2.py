def test_standard_case():
    # Test a standard case where tokens are refilled and the request is allowed
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=1.0
    )
    assert allowed == True
    assert remaining == 6.0
    assert new_last_refill == 1.0

def test_request_exceeds_capacity():
    # Test a case where the request exceeds the available tokens
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=10.0
    )
    assert allowed == False
    assert remaining == 7.0
    assert new_last_refill == 1.0

def test_no_refill_needed():
    # Test a case where no refill is needed and the request is allowed
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=10.0, last_refill_time=0.0, request_time=0.5, cost=1.0
    )
    assert allowed == True
    assert remaining == 9.0
    assert new_last_refill == 0.5

def test_refill_exceeds_capacity():
    # Test a case where refill exceeds the bucket capacity
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=20.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=1.0
    )
    assert allowed == True
    assert remaining == 9.0
    assert new_last_refill == 1.0

def test_zero_refill_rate():
    # Test a case where the refill rate is zero
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=10.0, refill_rate=0.0, refill_period=1.0, 
        current_tokens=5.0, last_refill_time=0.0, request_time=1.0, cost=1.0
    )
    assert allowed == True
    assert remaining == 4.0
    assert new_last_refill == 1.0

def test_zero_capacity():
    # Test a case where the bucket capacity is zero
    allowed, remaining, new_last_refill = evaluate_token_bucket(
        capacity=0.0, refill_rate=2.0, refill_period=1.0, 
        current_tokens=0.0, last_refill_time=0.0, request_time=1.0, cost=1.0
    )
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill == 1.0