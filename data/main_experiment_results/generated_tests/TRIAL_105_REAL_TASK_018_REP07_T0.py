# Test standard inputs
def test_circuit_breaker_closed_state():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 5, 0.0, 10.0, 30.0, True) == ("CLOSED", 0, 0.0)

def test_circuit_breaker_open_state():
    assert evaluate_circuit_breaker_transition("OPEN", 5, 5, 10.0, 30.0, 30.0, False) == ("OPEN", 5, 10.0)

def test_circuit_breaker_half_open_state():
    assert evaluate_circuit_breaker_transition("HALF_OPEN", 0, 5, 10.0, 40.0, 30.0, True) == ("CLOSED", 0, 0.0)

# Test edge cases
def test_circuit_breaker_zero_failure_threshold():
    assert evaluate_circuit_breaker_transition("CLOSED", 0, 0, 0.0, 10.0, 30.0, True) == ("OPEN", 1, 0.0)

def test_circuit_breaker_negative_failure_count():
    try:
        evaluate_circuit_breaker_transition("CLOSED", -1, 5, 0.0, 10.0, 30.0, True)
        assert False, "Expected ValueError for negative failure count"
    except ValueError:
        pass

def test_circuit_breaker_invalid_state():
    try:
        evaluate_circuit_breaker_transition("INVALID", 0, 5, 0.0, 10.0, 30.0, True)
        assert False, "Expected ValueError for invalid state"
    except ValueError:
        pass