def test_standard_input():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining >= 0.0

def test_zero_elapsed_time():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 0.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert remaining == current_tokens - cost if current_tokens >= cost else current_tokens

def test_insufficient_tokens():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 0.0
    last_refill_time = 0.0
    request_time = 0.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert not allowed
    assert remaining == current_tokens

def test_zero_capacity():
    capacity = 0.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 0.0
    last_refill_time = 0.0
    request_time = 0.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert not allowed
    assert remaining == 0.0

def test_negative_cost():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = -1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == current_tokens + abs(cost)

def test_zero_refill_rate():
    capacity = 10.0
    refill_rate = 0.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert remaining == current_tokens - cost if current_tokens >= cost else current_tokens