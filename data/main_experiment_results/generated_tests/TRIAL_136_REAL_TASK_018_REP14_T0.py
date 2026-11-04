# Test 1: CLOSED state with no failures
def test_closed_state_no_failures():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True)
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 2: CLOSED state with failures exceeding threshold
def test_closed_state_failures_exceed_threshold():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False)
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

# Test 3: OPEN state with recovery timeout not yet elapsed
def test_open_state_recovery_timeout_not_elapsed():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("OPEN", 3, 3, 10.0, 30.0, 30.0, True)
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

# Test 4: OPEN state with recovery timeout elapsed
def test_open_state_recovery_timeout_elapsed():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("OPEN", 3, 3, 10.0, 40.0, 30.0, True)
    assert state == "HALF_OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

# Test 5: HALF_OPEN state with successful call
def test_half_open_state_successful_call():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 10.0, 40.0, 30.0, True)
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 6: HALF_OPEN state with failed call
def test_half_open_state_failed_call():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 10.0, 40.0, 30.0, False)
    assert state == "OPEN"
    assert failure_count == 4
    assert last_failure_time == 40.0

test_closed_state_no_failures()
test_closed_state_failures_exceed_threshold()
test_open_state_recovery_timeout_not_elapsed()
test_open_state_recovery_timeout_elapsed()
test_half_open_state_successful_call()
test_half_open_state_failed_call()