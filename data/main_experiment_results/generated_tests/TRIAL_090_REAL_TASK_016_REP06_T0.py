def test_standard_request():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed == True
    assert remaining >= 4.0
    assert new_last_refill >= request_time

def test_insufficient_tokens():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 0.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill >= request_time

def test_zero_refill_rate():
    capacity = 10.0
    refill_rate = 0.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed == True if current_tokens >= cost else False
    assert remaining >= current_tokens - cost if allowed else current_tokens
    assert new_last_refill >= request_time

def test_negative_cost():
    capacity = 10.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = -1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed == True
    assert remaining >= current_tokens + 1.0
    assert new_last_refill >= request_time

def test_zero_capacity():
    capacity = 0.0
    refill_rate = 1.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed == False
    assert remaining == 0.0
    assert new_last_refill >= request_time

test_standard_request()
test_insufficient_tokens()
test_zero_refill_rate()
test_negative_cost()
test_zero_capacity()