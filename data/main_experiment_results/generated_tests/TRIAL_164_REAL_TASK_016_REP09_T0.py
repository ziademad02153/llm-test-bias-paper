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

def test_refill_period():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 2.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

def test_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

def test_negative_cost():
    try:
        evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0, cost=-1.0)
        assert False, "Expected an exception for negative cost"
    except Exception:
        assert True

def test_non_numeric_input():
    try:
        evaluate_token_bucket("a", 1.0, 1.0, 5.0, 0.0, 1.0)
        assert False, "Expected an exception for non-numeric input"
    except Exception:
        assert True