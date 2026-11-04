from typing import Optional, Tuple

def test_parse_github_url_standard_inputs():
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("http://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("https://www.github.com/user/repo") == ("user", "repo")

def test_parse_github_url_edge_cases():
    assert parse_github_url("https://github.com/user/repo.git") == ("user", "repo")
    assert parse_github_url("") is None
    assert parse_github_url("invalid_url") is None

def test_parse_github_url_invalid_urls():
    assert parse_github_url("https://gitlab.com/user/repo") is None
    assert parse_github_url("https://github.com/user") is None
    assert parse_github_url("https://github.com/") is None

def test_parse_github_url_www_prefix_and_git_extension():
    assert parse_github_url("https://www.github.com/user/repo.git") == ("user", "repo")
    assert parse_github_url("http://www.github.com/user/repo.git") == ("user", "repo")

def test_parse_github_url_http_https_prefixes():
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("http://github.com/user/repo") == ("user", "repo")