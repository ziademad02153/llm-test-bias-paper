def test_standard_input():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

def test_empty_bucket():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 1.0, cost=10.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

def test_zero_refill_rate():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 0.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining == 5.0
    assert new_last_refill == 0.0

def test_negative_cost():
    try:
        evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0, cost=-1.0)
        assert False, "Expected ValueError for negative cost"
    except ValueError:
        assert True

def test_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

def test_negative_refill_period():
    try:
        evaluate_token_bucket(10.0, 1.0, -1.0, 5.0, 0.0, 1.0)
        assert False, "Expected ValueError for negative refill period"
    except ValueError:
        assert True