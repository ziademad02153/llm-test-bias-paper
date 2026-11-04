def test_circuit_breaker_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 3, 10.0)

def test_circuit_breaker_half_open_state():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, True) == ("HALF_OPEN", 3, 0.0)

def test_circuit_breaker_recover_from_half_open():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_fail_from_half_open():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 4, 10.0)

def test_circuit_breaker_timeout():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, False) == ("HALF_OPEN", 3, 0.0)