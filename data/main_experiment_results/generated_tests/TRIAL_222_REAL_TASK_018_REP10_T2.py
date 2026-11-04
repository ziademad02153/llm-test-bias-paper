Here's a comprehensive suite of unit tests for the `evaluate_circuit_breaker_transition` function:

```python
def test_closed_state_successful_call_resets_counters():
    state = "CLOSED"
    failure_count = 2
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=failure_count,
        failure_threshold=3,
        last_failure_time=100.0,
        current_time=200.0,
        recovery_timeout=60.0,
        call_succeeded=True
    )
    assert result_state == "CLOSED"
    assert result_count == 0
    assert result_time == 0.0

def test_closed_state_failed_call_increments_count_and_opens_when_threshold_reached():
    state = "CLOSED"
    failure_count = 2
    current_time = 200.0
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=failure_count,
        failure_threshold=3,
        last_failure_time=100.0,
        current_time=current_time,
        recovery_timeout=60.0,
        call_succeeded=False
    )
    assert result_state == "OPEN"
    assert result_count == 3
    assert result_time == current_time

def test_open_state_transitions_to_half_open_after_timeout():
    state = "OPEN"
    last_failure_time = 100.0
    current_time = 200.0
    recovery_timeout = 60.0
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=3,
        failure_threshold=3,
        last_failure_time=last_failure_time,
        current_time=current_time,
        recovery_timeout=recovery_timeout,
        call_succeeded=False
    )
    assert result_state == "HALF_OPEN"
    assert result_count == 0
    assert result_time == 0.0

def test_half_open_state_successful_call_transitions_to_closed():
    state = "HALF_OPEN"
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=200.0,
        recovery_timeout=60.0,
        call_succeeded=True
    )
    assert result_state == "CLOSED"
    assert result_count == 0
    assert result_time == 0.0

def test_half_open_state_failed_call_transitions_to_open():
    state = "HALF_OPEN"
    current_time = 200.0
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=0,
        failure_threshold=3,
        last_failure_time=0.0,
        current_time=current_time,
        recovery_timeout=60.0,
        call_succeeded=False
    )
    assert result_state == "OPEN"
    assert result_count == 1
    assert result_time == current_time

def test_open_state_remains_open_before_timeout():
    state = "OPEN"
    last_failure_time = 100.0
    current_time = 150.0
    recovery_timeout = 60.0
    result_state, result_count, result_time = evaluate_circuit_breaker_transition(
        state=state,
        failure_count=3,
        failure_threshold=3,
        last_failure_time=last_f