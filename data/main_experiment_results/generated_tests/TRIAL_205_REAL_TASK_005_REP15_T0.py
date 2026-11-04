def test_split_host_port_standard():
    assert split_host_port("example.com:80") == ("example.com", "80")

def test_split_host_port_no_port():
    assert split_host_port("example.com") == ("example.com", "")

def test_split_host_port_ipv4():
    assert split_host_port("192.168.1.1:443") == ("192.168.1.1", "443")

def test_split_host_port_ipv6():
    assert split_host_port("[2001:db8::1]:8080") == ("2001:db8::1", "8080")

def test_split_host_port_ipv6_no_port():
    assert split_host_port("[2001:db8::1]") == ("2001:db8::1", "")

def test_split_host_port_with_userinfo():
    assert split_host_port("user:pass@example.com:80") == ("example.com", "80")

def test_split_host_port_empty_input():
    assert split_host_port("") == ("", "")

def test_split_host_port_only_colon():
    assert split_host_port(":") == ("", "")