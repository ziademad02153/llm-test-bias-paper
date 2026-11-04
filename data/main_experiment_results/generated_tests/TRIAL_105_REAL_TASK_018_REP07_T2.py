def test_closed_state_successful_call_resets_failure_count():
    state = CircuitBreakerState.CLOSED
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 101.0
    recovery_timeout = 10.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == CircuitBreakerState.CLOSED
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_closed_state_failed_call_increments_failure_count():
    state = CircuitBreakerState.CLOSED
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 101.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == CircuitBreakerState.OPEN
    assert new_failure_count == 3
    assert new_last_failure_time == current_time

def test_open_state_transitions_to_half_open_after_timeout():
    state = CircuitBreakerState.OPEN
    failure_count = 3
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 110.1  # 0.1 over recovery_timeout
    recovery_timeout = 10.0
    call_succeeded = False  # Should not matter in OPEN state
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == CircuitBreakerState.HALF_OPEN
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_successful_call_transitions_to_closed():
    state = CircuitBreakerState.HALF_OPEN
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 110.0
    recovery_timeout = 10.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == CircuitBreakerState.CLOSED
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_failed_call_transitions_to_open():
    state = CircuitBreakerState.HALF_OPEN
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 110.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure