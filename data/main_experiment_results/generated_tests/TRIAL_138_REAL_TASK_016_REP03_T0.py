def test_standard_token_bucket_request():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0

def test_token_bucket_request_exceeds_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 1.0, cost=11.0)
    assert allowed == False
    assert remaining == 0.0

def test_token_bucket_refill():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 2.0)
    assert allowed == True
    assert remaining > 0.0

def test_token_bucket_zero_refill_rate():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 0.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining == 5.0

def test_token_bucket_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0

def test_token_bucket_negative_cost():
    try:
        evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0, cost=-1.0)
        assert False, "Expected an exception for negative cost"
    except Exception:
        assert True