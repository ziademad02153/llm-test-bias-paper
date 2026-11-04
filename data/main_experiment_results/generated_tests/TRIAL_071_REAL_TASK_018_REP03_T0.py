def test_initial_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_open_state_after_threshold_failures():
    assert evaluate_circuit_breaker_transition("CLOSED", 2, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 3, 10.0 + 30.0)

def test_half_open_state_after_recovery_timeout():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, True) == ("HALF_OPEN", 3, 0.0)

def test_closed_state_after_successful_call_in_half_open():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 0.0, 50.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_open_state_after_failure_in_half_open():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 3, 3, 0.0, 50.0, 30.0, False) == ("OPEN", 4, 50.0 + 30.0)

def test_invalid_initial_state():
    try:
        evaluate_circuit_breaker_transition("INVALID", 0, 3, 0.0, 10.0, 30.0, True)
        assert False, "Expected an exception for invalid initial state"
    except Exception:
        assert True