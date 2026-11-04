def test_standard_input():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

def test_insufficient_tokens():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

def test_zero_refill_rate():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 0.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

def test_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

def test_negative_input():
    try:
        evaluate_token_bucket(-10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
        assert False, "Expected ValueError for negative capacity"
    except ValueError:
        pass

def test_non_numeric_input():
    try:
        evaluate_token_bucket("ten", 1.0, 1.0, 5.0, 0.0, 1.0)
        assert False, "Expected TypeError for non-numeric input"
    except TypeError:
        pass