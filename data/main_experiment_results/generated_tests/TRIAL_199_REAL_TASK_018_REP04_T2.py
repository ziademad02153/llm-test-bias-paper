def test_closed_state_successful_call_resets_failure_count():
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 30.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_closed_state_failed_call_increments_failure_count_and_opens_when_threshold_reached():
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 30.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "OPEN"
    assert new_failure_count == 3
    assert new_last_failure_time == 200.0

def test_open_state_transitions_to_half_open_after_recovery_timeout():
    state = "OPEN"
    failure_count = 3
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 131.0  # 31 seconds later (recovery_timeout is 30)
    recovery_timeout = 30.0
    call_succeeded = False  # Irrelevant in OPEN state
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "HALF_OPEN"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_successful_call_transitions_to_closed():
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 200.0
    recovery_timeout = 30.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_failed_call_transitions_to_open():
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 200.0
    recovery_timeout = 30.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_time