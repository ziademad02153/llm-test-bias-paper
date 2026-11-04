def test_standard_input():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed
    assert remaining > 0.0

def test_insufficient_tokens():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert not allowed
    assert remaining == 0.0

def test_refill_period_elapsed():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 2.0)
    assert allowed
    assert remaining > 0.0

def test_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert not allowed
    assert remaining == 0.0

def test_zero_refill_rate():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 0.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed
    assert remaining == 5.0

def test_negative_input():
    try:
        evaluate_token_bucket(-10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
        assert False, "Expected ValueError for negative capacity"
    except ValueError:
        pass