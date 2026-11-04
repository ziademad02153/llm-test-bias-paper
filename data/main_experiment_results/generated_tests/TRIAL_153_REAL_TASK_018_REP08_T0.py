def test_circuit_breaker_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 3, 10.0)

def test_circuit_breaker_half_open_state():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, True) == ("HALF_OPEN", 0, 0.0)

def test_circuit_breaker_failure_count_reset():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 1, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state_persistence():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 20.0, 30.0, False) == ("OPEN", 4, 20.0)

def test_circuit_breaker_recovery_timeout():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, False) == ("HALF_OPEN", 3, 0.0)