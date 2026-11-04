# Test standard inputs
def test_circuit_breaker_closed_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True)
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("OPEN", 3, 3, 10.0, 10.0, 30.0, False)
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

def test_circuit_breaker_half_open_state():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("HALF_OPEN", 0, 3, 0.0, 40.0, 30.0, True)
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_transition_to_open():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False)
    assert state == "OPEN"
    assert failure_count == 3
    assert last_failure_time == 10.0

def test_circuit_breaker_transition_to_half_open():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("OPEN", 0, 3, 10.0, 40.0, 30.0, True)
    assert state == "HALF_OPEN"
    assert failure_count == 0
    assert last_failure_time == 0.0

def test_circuit_breaker_edge_case():
    state, failure_count, last_failure_time = evaluate_circuit_breaker_transition("CLOSED", 0, 0, 0.0, 10.0, 0.0, True)
    assert state == "CLOSED"
    assert failure_count == 0
    assert last_failure_time == 0.0