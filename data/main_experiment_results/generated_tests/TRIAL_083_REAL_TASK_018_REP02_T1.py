from enum import Enum

class CircuitBreakerState(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

def test_circuit_breaker_closed_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 3, 0.0, 10.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 3, 0.0, 10.0, 30.0, False)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 1
    assert last_failure_time == 10.0

    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 2, 3, 0.0, 10.0, 30.0, False)
    assert state == CircuitBreakerState.OPEN
    assert failure_count == 3
    assert last_failure_time == 10.0

def test_circuit_breaker_half_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.OPEN, 0, 3, 0.0, 40.0, 30.0, True)
    assert state == CircuitBreakerState.HALF_OPEN
    assert failure_count == 0
    assert last_failure_time == 0.0

    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.HALF_OPEN, 0, 3, 0.0, 10.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.HALF_OPEN, 0, 3, 0.0, 10.0, 30.0, False)
    assert state == CircuitBreakerState.OPEN
    assert failure_count == 1
    assert last_failure_time == 10.0

def test_circuit_breaker_edge_cases():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, 0, 0, 0.0, 10.0, 30.0, True)
    assert state == CircuitBreakerState.CLOSED
    assert failure_count == 0
    assert last_failure_time == 0.0

    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition(CircuitBreakerState.OPEN, 0, 0, 0.0, 10.0, 0.0, True)
    assert state == CircuitBreakerState.HALF_OPEN
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_invalid_inputs():
    try:
        evaluate_circuit_breaker_transition("INVALID_STATE", 0, 3, 0.0, 10.0, 30.0, True)
        assert False, "Expected ValueError for invalid state"
    except ValueError:
        assert True

    try:
        evaluate_circuit_breaker_transition(CircuitBreakerState.CLOSED, -1, 3, 0.0,