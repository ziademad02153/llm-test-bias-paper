def test_closed_state_failure_below_threshold():
    """Test CLOSED state with a failure but below threshold."""
    state = "CLOSED"
    failure_count = 1
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 101.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 2
    assert new_last_failure_time == 101.0

def test_closed_state_failure_above_threshold():
    """Test CLOSED state with failures exceeding threshold."""
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 2
    last_failure_time = 100.0
    current_time = 101.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "OPEN"
    assert new_failure_count == 3
    assert new_last_failure_time == 101.0

def test_open_state_timeout_not_expired():
    """Test OPEN state with timeout not expired."""
    state = "OPEN"
    failure_count = 3
    failure_threshold = 2
    last_failure_time = 100.0
    current_time = 105.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "OPEN"
    assert new_failure_count == 3
    assert new_last_failure_time == 100.0

def test_open_state_timeout_expired():
    """Test OPEN state with timeout expired, transitioning to HALF_OPEN."""
    state = "OPEN"
    failure_count = 3
    failure_threshold = 2
    last_failure_time = 100.0
    current_time = 115.0
    recovery_timeout = 10.0
    call_succeeded = False
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "HALF_OPEN"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_success():
    """Test HALF_OPEN state with successful call, transitioning to CLOSED."""
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 2
    last_failure_time = 0.0
    current_time = 115.0
    recovery_timeout = 10.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last