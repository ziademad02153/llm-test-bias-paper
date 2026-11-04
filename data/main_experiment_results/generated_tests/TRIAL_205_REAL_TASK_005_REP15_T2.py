import unittest
from your_module import split_host_port  # Replace 'your_module' with the actual module name

def test_standard_input():
    assert split_host_port('example.com:8080') == ('example.com', '8080')

def test_ipv6_input():
    assert split_host_port('[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:8080') == ('[2001:0db8:85a3:0000:0000:8a2e:0370:7334]', '8080')

def test_userinfo_input():
    assert split_host_port('user:pass@example.com:8080') == ('example.com', '8080')

def test_empty_port_input():
    assert split_host_port('example.com') == ('example.com', '')

def test_empty_input():
    assert split_hostport('') == ('', '')

def test_invalid_input():
    assert split_hostport('example.com:8080:1234') == ('example.com:8080:1234', '')

# Run the tests
test_standard_input()
test_ipv6_input()
test_userinfo_input()
test_empty_port_input()
test_empty_input()
test_invalid_input()