def test_closed_to_open_on_failure_threshold():
    """Test transition from CLOSED to OPEN when failure count reaches threshold."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=2,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "CLOSED"  # Not yet at threshold
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"  # Reached threshold


def test_open_to_half_open_after_timeout():
    """Test transition from OPEN to HALF_OPEN after recovery timeout."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=4.0,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"  # Timeout not yet passed
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=5.1,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "HALF_OPEN"  # Timeout passed


def test_half_open_to_closed_on_success():
    """Test transition from HALF_OPEN to CLOSED on successful call."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=5.1,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert new_state == "CLOSED"
    assert new_count == 0  # Counter should reset


def test_half_open_to_open_on_failure():
    """Test transition from HALF_OPEN to OPEN on failed call."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="HALF_OPEN",
        failure_count=3,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=5.1,
        recovery_timeout=5.0,
        call_succeeded=False
    )
    assert new_state == "OPEN"
    assert new_time == 5.1  # Last failure time should update


def test_closed_reset_on_success():
    """Test failure count resets on success in CLOSED state."""
    new_state, new_count, new_time = evaluate_circuit_breaker_transition(
        state="CLOSED",
        failure_count=1,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=1.0,
        recovery_timeout=5.0,
        call_succeeded=True
    )
    assert new_count == 0  # Counter should reset