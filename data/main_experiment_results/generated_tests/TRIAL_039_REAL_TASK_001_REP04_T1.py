from typing import Optional, Tuple

def test_standard_github_url() -> None:
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")

def test_github_url_with_www_prefix() -> None:
    assert parse_github_url("https://www.github.com/user/repo") == ("user", "repo")

def test_github_url_with_git_extension() -> None:
    assert parse_github_url("https://github.com/user/repo.git") == ("user", "repo")

def test_invalid_github_url() -> None:
    assert parse_github_url("https://example.com/user/repo") is None

def test_empty_github_url() -> None:
    assert parse_github_url("") is None

def test_github_url_with_invalid_path() -> None:
    assert parse_github_url("https://github.com/user") is None