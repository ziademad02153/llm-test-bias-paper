from typing import Tuple

def test_standard_host_port():
    assert split_host_port("example.com:8080") == ("example.com", "8080")

def test_ipv6_host_port():
    assert split_host_port("[::1]:8080") == ("[::1]", "8080")

def test_userinfo_host_port():
    assert split_host_port("user:pass@example.com:8080") == ("example.com", "8080")

def test_empty_input():
    assert split_host_port("") == ("", "")

def test_host_only():
    assert split_host_port("example.com") == ("example.com", "")

def test_ipv6_host_only():
    assert split_host_port("[::1]") == ("[::1]", "")