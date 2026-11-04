# Test 1: Transition from CLOSED to OPEN when failure_count exceeds failure_threshold
def test_closed_to_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=5,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=10.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 6
    assert last_failure_time == 10.0

# Test 2: Transition from OPEN to HALF_OPEN after recovery_timeout
def test_open_to_half_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=6,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=16.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "HALF_OPEN"
    assert failure_count == 6
    assert last_failure_time == 10.0

# Test 3: Transition from HALF_OPEN to CLOSED on successful call
def test_half_open_to_closed_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=6,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=16.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 10.0

# Test 4: Transition from HALF_OPEN to OPEN on failed call
def test_half_open_to_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=6,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=16.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 7
    assert last_failure_time == 16.0

# Test 5: Stay in CLOSED state on successful call
def test_closed_state_on_success():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=10.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 6: Stay in OPEN state if recovery_timeout has not passed
def test_open_state_before_timeout():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=6,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=14.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 6
    assert last_failure_time == 10.0