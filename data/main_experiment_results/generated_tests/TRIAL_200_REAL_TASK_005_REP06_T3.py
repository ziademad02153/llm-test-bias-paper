from typing import Tuple

def test_standard_host_port():
    assert split_host_port("example.com:8080") == ("example.com", "8080")

def test_ipv6_host_port():
    assert split_host_port("[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:8080") == ("[2001:0db8:85a3:0000:0000:8a2e:0370:7334]", "8080")

def test_userinfo_host_port():
    assert split_host_port("user:pass@example.com:8080") == ("example.com", "8080")

def test_empty_input():
    assert split_host_port("") == ("", "")

def test_host_only():
    assert split_host_port("example.com") == ("example.com", "")

def test_ipv6_host_only():
    assert split_host_port("[2001:0db8:85a3:0000:0000:8a2e:0370:7334]") == ("[2001:0db8:85a3:0000:0000:8a2e:0370:7334]", "")