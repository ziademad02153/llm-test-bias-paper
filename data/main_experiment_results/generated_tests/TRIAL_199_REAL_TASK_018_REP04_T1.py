from enum import Enum
from typing import Tuple

class CircuitBreakerState(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

def test_circuit_breaker_closed_state():
    state = CircuitBreakerState.CLOSED
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 10.0
    recovery_timeout = 30.0
    call_succeeded = True
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == CircuitBreakerState.CLOSED
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_circuit_breaker_open_state():
    state = CircuitBreakerState.CLOSED
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 10.0
    recovery_timeout = 30.0
    call_succeeded = False
    for _ in range(failure_threshold):
        state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert state == CircuitBreakerState.OPEN
    assert failure_count == failure_threshold
    assert last_failure_time == current_time

def test_circuit_breaker_half_open_state():
    state = CircuitBreakerState.OPEN
    failure_count = 3
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 30.0
    recovery_timeout = 30.0
    call_succeeded = True
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert state == CircuitBreakerState.HALF_OPEN
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_recovery():
    state = CircuitBreakerState.HALF_OPEN
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 10.0
    recovery_timeout = 30.0
    call_succeeded = True
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == CircuitBreakerState.CLOSED
    assert new_failure_count == 0
    assert new_last_failure_time == 0.0

def test_circuit_breaker_failure():
    state = CircuitBreakerState.HALF_OPEN
    failure_count = 0
    failure_threshold = 3
    last_failure_time = 0.0
    current_time = 10.0
    recovery_timeout = 30.0
    call_succeeded = False
    new_state, new_failure_count, new_last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, failure_threshold, last_failure_time, current_time, recovery_timeout, call_succeeded)
    assert new_state == CircuitBreakerState.OPEN
    assert new_failure_count == 1
    assert new_last_failure_time == current_time

test_circuit_breaker_closed_state()
test_circuit_breaker_open_state()
test_circuit_breaker_half_open_state()
test_circuit_breaker_recovery()
test_circuit_breaker_failure()