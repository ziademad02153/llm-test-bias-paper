# Test standard input
def test_standard_input():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

# Test edge case: empty bucket
def test_empty_bucket():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

# Test edge case: zero refill rate
def test_zero_refill_rate():
    allowed, remaining, new_last_refill = evaluate_token_bucket(10.0, 0.0, 1.0, 5.0, 0.0, 1.0)
    assert allowed == True
    assert remaining > 0.0
    assert new_last_refill > 0.0

# Test edge case: zero capacity
def test_zero_capacity():
    allowed, remaining, new_last_refill = evaluate_token_bucket(0.0, 1.0, 1.0, 0.0, 0.0, 1.0)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill > 0.0

# Test edge case: negative cost
def test_negative_cost():
    try:
        evaluate_token_bucket(10.0, 1.0, 1.0, 5.0, 0.0, 1.0, cost=-1.0)
        assert False, "Expected ValueError for negative cost"
    except ValueError:
        assert True

# Test edge case: negative capacity
def test_negative_capacity():
    try:
        evaluate_token_bucket(-10.0, 1.0, 1.0, 5.0, 0.0, 1.0)
        assert False, "Expected ValueError for negative capacity"
    except ValueError:
        assert True