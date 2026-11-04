# Test 1: Transition from CLOSED to OPEN when failure count exceeds threshold
def test_closed_to_open_transition():
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 1.0
    recovery_timeout = 5.0
    call_succeeded = False
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == "OPEN"
    assert new_failure_count == 3
    assert new_last_failure_time == 1.0

# Test 2: Transition from OPEN to HALF_OPEN after recovery timeout
def test_open_to_half_open_transition():
    state = "OPEN"
    failure_count = 3
    failure_threshold = 3
    last_failure_time = 1.0
    current_time = 6.0
    recovery_timeout = 5.0
    call_succeeded = False
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == "HALF_OPEN"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

# Test 3: Transition from HALF_OPEN to CLOSED on successful call
def test_half_open_to_closed_transition():
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 6.0
    recovery_timeout = 5.0
    call_succeeded = True
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == "CLOSED"
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

# Test 4: Transition from HALF_OPEN to OPEN on failed call
def test_half_open_to_open_transition():
    state = "HALF_OPEN"
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 6.0
    recovery_timeout = 5.0
    call_succeeded = False
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == "OPEN"
    assert new_failure_count == 1
    assert new_last_failure_time == 6.0

# Test 5: Reset failure count on successful call in CLOSED state
def test_reset_failure_count_on_success_in_closed():
    state = "CLOSED"
    failure_count = 2
    failure_threshold = 3
    last_failure_time = 1.0
    current_time = 2.0
    recovery_timeout = 5.0
    call_succeeded = True
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold