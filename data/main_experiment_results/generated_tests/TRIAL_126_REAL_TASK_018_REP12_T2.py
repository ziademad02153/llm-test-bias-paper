def test_closed_state_successful_call_resets_failure_count():
    """Test that a successful call in CLOSED state resets failure count."""
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 50.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_closed_state_failed_call_increments_failure_count():
    """Test that a failed call in CLOSED state increments failure count."""
    state = "CLOSED"
    failure_count = 1
    failure_threshold = 2
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 50.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "OPEN"
    assert new_failure_count == 2
    assert new_last_failure_time == current_time

def test_open_state_transitions_to_half_open_after_timeout():
    """Test that OPEN state transitions to HALF_OPEN after recovery timeout."""
    state = "OPEN"
    failure_count = 3
    failure_threshold = 2
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 50.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "HALF_OPEN"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_successful_call_transitions_to_closed():
    """Test that a successful call in HALF_OPEN state transitions to CLOSED."""
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 2
    last_failure_time = 0.0
    current_time = 200.0
    recovery_timeout = 50.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_failed_call_transitions_to_open():
    """Test that a failed call in HALF_OPEN state transitions to OPEN."""
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 2
    last_failure_time = 0.0
    current_time = 200.0
    recovery_timeout = 50.0