from typing import Optional, Tuple

def test_parse_github_url_standard():
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("http://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("https://www.github.com/user/repo") == ("user", "repo")

def test_parse_github_url_extensions():
    assert parse_github_url("https://github.com/user/repo.git") == ("user", "repo")
    assert parse_github_url("https://github.com/user/repo.git/") == ("user", "repo")

def test_parse_github_url_invalid():
    assert parse_github_url("") is None
    assert parse_github_url("https://example.com") is None
    assert parse_github_url("https://github.com") is None
    assert parse_github_url("https://github.com/user") is None

def test_parse_github_url_edge_cases():
    assert parse_github_url("https://github.com/") is None
    assert parse_github_url("https://github.com//") is None
    assert parse_github_url("https://github.com/user/") is None
    assert parse_github_url("https://github.com/user//") is None