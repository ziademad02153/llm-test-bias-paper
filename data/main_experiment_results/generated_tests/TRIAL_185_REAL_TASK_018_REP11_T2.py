def test_closed_state_successful_call():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=10.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_closed_state_failed_call_below_threshold():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=1,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=10.0,
        call_succeeded=False
    )
    assert state == "CLOSED"
    assert failure_count == 2
    assert last_failure_time == 1.0

def test_closed_state_failed_call_above_threshold():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=10.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 1.0

def test_open_state_recovery_timeout_not_expired():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=1.0,
        current_time=5.0,
        recovery_timeout=10.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 1.0

def test_open_state_recovery_timeout_expired():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=1.0,
        current_time=12.0,
        recovery_timeout=10.0,
        call_succeeded=False
    )
    assert state == "HALF_OPEN"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_half_open_state_successful_call():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=10.0,
        call_succeeded=True
    )
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_half_open_state_failed_call():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=10.0,
        call_succeeded=False
    )
    assert state == "OPEN"
    assert failure_count == 1
    assert last_failure