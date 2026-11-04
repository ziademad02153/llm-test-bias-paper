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
    assert remaining == 9.0
    assert new_last_refill == request_time

def test_insufficient_tokens():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 0.0
    last_refill_time = 0.0
    request_time = 0.1
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert not allowed
    assert remaining == 0.5
    assert new_last_refill == request_time

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
    assert new_last_refill == request_time

def test_zero_cost():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 0.0
    request_time = 1.0
    cost = 0.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 9.5
    assert new_last_refill == request_time

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
    assert remaining == 10.5
    assert new_last_refill == request_time

def test_edge_case_zero_elapsed_time():
    capacity = 10.0
    refill_rate = 5.0
    refill_period = 1.0
    current_tokens = 5.0
    last_refill_time = 1.0
    request_time = 1.0
    cost = 1.0
    allowed, remaining, new_last_refill = evaluate_token_bucket(capacity, refill_rate, refill_period, current_tokens, last_refill_time, request_time, cost)
    assert allowed
    assert remaining == 4.0
    assert new_last_refill == request_time