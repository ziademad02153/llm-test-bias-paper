from typing import Tuple

def test_standard_input():
    assert split_host_port("example.com:8080") == ("example.com", "8080")

def test_ipv6_address():
    assert split_host_port("[::1]:8080") == ("[::1]", "8080")

def test_userinfo_present():
    assert split_host_port("user:pass@example.com:8080") == ("example.com", "8080")

def test_empty_input():
    assert split_host_port("") == ("", "")

def test_no_port():
    assert split_host_port("example.com") == ("example.com", "")

def test_ipv6_address_no_port():
    assert split_host_port("[::1]") == ("[::1]", "")

def test_userinfo_no_port():
    assert split_host_port("user:pass@example.com") == ("example.com", "")

def test_invalid_input():
    assert split_host_port("invalid_input") == ("invalid_input", "")

def test_empty_host():
    assert split_host_port(":8080") == ("", "8080")

def test_empty_port():
    assert split_host_port("example.com:") == ("example.com", "")