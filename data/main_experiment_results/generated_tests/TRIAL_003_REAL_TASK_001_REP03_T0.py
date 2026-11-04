from typing import Optional, Tuple

def test_standard_github_url():
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")

def test_github_url_with_www_prefix():
    assert parse_github_url("https://www.github.com/user/repo") == ("user", "repo")

def test_github_url_with_git_extension():
    assert parse_github_url("https://github.com/user/repo.git") == ("user", "repo")

def test_invalid_github_url():
    assert parse_github_url("https://example.com/user/repo") is None

def test_empty_github_url():
    assert parse_github_url("") is None

def test_github_url_with_http_prefix():
    assert parse_github_url("http://github.com/user/repo") == ("user", "repo")