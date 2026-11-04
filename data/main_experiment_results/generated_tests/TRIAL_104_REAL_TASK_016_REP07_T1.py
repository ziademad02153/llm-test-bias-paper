def test_standard_input():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 6.0

def test_insufficient_tokens():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 0.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert not allowed
    assert remaining == 1.0

def test_zero_refill_rate():
    capacity = 10.0
    refill_rate = 0.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 4.0

def test_zero_refill_period():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 0.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 5.0

def test_negative_cost():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = -1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 6.0

def test_zero_cost():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 0.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 6.0

test_standard_input()
test_insufficient_tokens()
test_zero_refill_rate()
test_zero_refill_period()
test_negative_cost()
test_zero_cost()