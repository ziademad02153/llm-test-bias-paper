def test_closed_to_open_on_failure_threshold():
    """Test transition from CLOSED to OPEN when failure count reaches threshold."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 3  # failure_count increments

def test_open_to_half_open_after_timeout():
    """Test transition from OPEN to HALF_OPEN after recovery timeout."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=6.0,  # exceeds recovery_timeout=5.0
        recovery_timeout=5.0,
        call_succeeded=False  # irrelevant for OPEN->HALF_OPEN transition
    )
    assert new_state == "HALF_OPEN"
    assert new_count == 0  # reset on half-open

def test_half_open_to_closed_on_success():
    """Test transition from HALF_OPEN to CLOSED on successful call."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert new_state == "CLOSED"
    assert new_count == 0  # remains reset

def test_half_open_to_open_on_failure():
    """Test transition from HALF_OPEN to OPEN on failed call."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 1  # increments on half-open failure

def test_closed_increments_failure_count():
    """Test CLOSED state increments failure count but doesn't transition yet."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=1,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "CLOSED"
    assert new_count == 2  # increments but below threshold

def test_open_remains_open_before_timeout():
    """Test OPEN state remains unchanged if timeout not reached."""
    new_state, new_count, _ = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=4.0,  # below recovery_timeout=5.0
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_count == 3  # unchanged