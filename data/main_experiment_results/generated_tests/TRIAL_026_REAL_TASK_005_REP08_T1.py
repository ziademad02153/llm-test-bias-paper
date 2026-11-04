def test_standard_host_port():
    assert split_host_port("example.com:80") == ("example.com", "80")

def test_ipv4_host_no_port():
    assert split_host_port("192.168.1.1") == ("192.168.1.1", "")

def test_ipv6_host_with_port():
    assert split_host_port("[2001:db8::1]:8080") == ("[2001:db8::1]", "8080")

def test_ipv6_host_no_port():
    assert split_host_port("[2001:db8::1]") == ("[2001:db8::1]", "")

def test_userinfo_and_port():
    assert split_host_port("user:pass@example.com:8080") == ("example.com", "8080")

def test_empty_input():
    assert split_host_port("") == ("", "")

def test_only_colon():
    assert split_host_port(":") == ("", "")

def test_only_brackets():
    assert split_host_port("") == ("[]", "")