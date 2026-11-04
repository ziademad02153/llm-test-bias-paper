def test_closed_state_failure_below_threshold():
    """Test CLOSED state with a failure that doesn't reach the threshold."""
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
    """Test CLOSED state transitioning to OPEN when failure count exceeds threshold."""
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
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

def test_open_state_transition_to_half_open():
    """Test OPEN state transitioning to HALF_OPEN after recovery timeout."""
    state = "OPEN"
    failure_count = 3
    failure_threshold = 3
    last_failure_time = 100.0
    current_time = 111.0  # 11 seconds later (exceeds recovery_timeout of 10)
    recovery_timeout = 10.0
    call_succeeded = False  # Should not matter in OPEN state
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "HALF_OPEN"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_success():
    """Test HALF_OPEN state transitioning to CLOSED on successful call."""
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 111.0
    recovery_timeout = 10.0
    call_succeeded = True
    
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(
        state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded
    )
    
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_half_open_state_failure():
    """Test HALF_OPEN state transitioning to OPEN on failed call."""
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 111.0
    recovery_timeout = 10.0
    call