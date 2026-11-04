# Test 1: Transition from CLOSED to OPEN when failure count exceeds threshold
def test_closed_to_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=10.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

# Test 2: Transition from OPEN to HALF_OPEN after recovery timeout
def test_open_to_half_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=5.0,
        current_time=15.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "HALF_OPEN"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 3: Transition from HALF_OPEN to CLOSED on successful call
def test_half_open_to_closed_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=20.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 4: Transition from HALF_OPEN to OPEN on failed call
def test_half_open_to_open_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=20.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 1
    assert last_failure_time == 20.0

# Test 5: Reset failure count on successful call in CLOSED state
def test_closed_reset_failure_count():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=20.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

# Test 6: Stay in OPEN state if recovery timeout has not expired
def test_open_state_no_transition():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=10.0,
        current_time=12.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0