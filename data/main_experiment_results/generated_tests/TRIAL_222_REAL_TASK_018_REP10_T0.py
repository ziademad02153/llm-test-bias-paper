def test_circuit_breaker_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 3, 10.0)

def test_circuit_breaker_half_open_state():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, True) == ("HALF_OPEN", 3, 0.0)

def test_circuit_breaker_recovery():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_failure_threshold():
    assert evaluate_circuit_breaker_transition("CLOSED", 2, 3, 0.0, 10.0, 30.0, False) == ("CLOSED", 3, 0.0)

def test_circuit_breaker_invalid_state():
    try:
        evaluate_circuit_breaker_transition("INVALID", 0, 3, 0.0, 10.0, 30.0, True)
        assert False, "Expected exception for invalid state"
    except Exception:
        assert True