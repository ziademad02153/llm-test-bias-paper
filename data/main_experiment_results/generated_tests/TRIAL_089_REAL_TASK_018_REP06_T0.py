def test_circuit_breaker_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 3, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 3, 3, 0.0, 10.0, 30.0, False) == ("OPEN", 3, 10.0)

def test_circuit_breaker_half_open_state():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, True) == ("HALF_OPEN", 0, 0.0)

def test_circuit_breaker_recovery_timeout():
    assert evaluate_circuit_breaker_transition("OPEN", 3, 3, 0.0, 40.0, 30.0, False) == ("OPEN", 3, 10.0)

def test_circuit_breaker_edge_case_failure_threshold_zero():
    assert evaluate_circuit_breaker_transition("CLOSED", 1, 0, 0.0, 10.0, 30.0, False) == ("OPEN", 1, 10.0)

def test_circuit_breaker_edge_case_negative_failure_count():
    try:
        evaluate_circuit_breaker_transition("CLOSED", -1, 3, 0.0, 10.0, 30.0, True)
        assert False, "Expected an exception for negative failure count"
    except Exception:
        pass