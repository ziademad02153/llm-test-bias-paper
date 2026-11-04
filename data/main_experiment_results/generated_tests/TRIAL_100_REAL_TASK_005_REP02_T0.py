def test_standard_ipv4():
    assert split_host_port("example.com:80") == ("example.com", "80")

def test_ipv6_without_brackets():
    assert split_host_port("2001:db8::1:80") == ("2001:db8::1", "80")

def test_ipv6_with_brackets():
    assert split_host_port("[2001:db8::1]:80") == ("2001:db8::1", "80")

def test_no_port():
    assert split_host_port("example.com") == ("example.com", "")

def test_userinfo_ipv4():
    assert split_host_port("user:pass@example.com:80") == ("example.com", "80")

def test_userinfo_ipv6():
    assert split_host_port("user:pass@[2001:db8::1]:80") == ("2001:db8::1", "80")

def test_empty_input():
    assert split_host_port("") == ("", "")

def test_only_brackets():
    assert split_host_port("[]") == ("", "")