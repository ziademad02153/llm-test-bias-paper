def test_closed_to_open_on_failure_threshold():
    """Transition from CLOSED to OPEN when failure count reaches threshold."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 0
    assert new_time == 1.0

def test_open_to_half_open_after_timeout():
    """Transition from OPEN to HALF_OPEN after recovery timeout."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=1.0,
        current_time=6.1,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "HALF_OPEN"
    assert new_count == 0
    assert new_time == 6.1

def test_half_open_to_closed_on_success():
    """Transition from HALF_OPEN to CLOSED on successful call."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=6.1,
        current_time=7.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert new_state == "CLOSED"
    assert new_count == 0
    assert new_time == 7.0

def test_half_open_to_open_on_failure():
    """Transition from HALF_OPEN to OPEN on failed call."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=6.1,
        current_time=7.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 0
    assert new_time == 7.0

def test_closed_increments_failure_count():
    """Increment failure count in CLOSED state on failure (below threshold)."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=1,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "CLOSED"
    assert new_count == 2
    assert new_time == 1.0

def test_open_remains_open_before_timeout():
    """Stay in OPEN state if timeout hasn't elapsed."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=1.0,
        current_time=5.9,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 0
    assert new_time == 1.0