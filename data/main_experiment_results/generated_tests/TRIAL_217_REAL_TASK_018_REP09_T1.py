from enum import Enum
from typing import Tuple

class CircuitBreakerState(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

def evaluate_circuit_breaker_transition(state: str, failure_count: int, failure_threshold: int, last_failure_time: float, current_time: float, recovery_timeout: float, call_succeeded: bool) -> Tuple[str, int, float]:
    # implementation under test...

def test_circuit_breaker_closed_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 3, 0.0, 10.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 3, 0.0, 10.0, 30.0, False)
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, 3, last_failure_time, 10.0, 30.0, False)
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, 3, last_failure_time, 10.0, 30.0, False)
    assert state == CircuitBreakerState.OPEN
    assert failure_count == 3
    assert last_failure_time == 10.0

def test_circuit_breaker_half_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.OPEN, 3, 3, 0.0, 10.0, 30.0, True)
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, 3, last_failure_time, 40.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_recovery_timeout():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.OPEN, 3, 3, 0.0, 10.0, 30.0, True)
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(state, failure_count, 3, last_failure_time, 40.0, 30.0, True)
    assert state == CircuitBreakerState.HALF_OPEN
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_edge_case_failure_threshold():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 1, 0.0, 10.0, 30.0, False)
    assert state == CircuitBreakerState.OPEN
    assert failure_count == 1
    assert last_failure_time == 10.0

def test_circuit_breaker_edge_case_zero_failure_count():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 3, 0.0, 10.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

test_circuit_breaker_closed_state()
test_circuit_break