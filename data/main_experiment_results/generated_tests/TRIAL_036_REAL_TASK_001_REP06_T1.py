from typing import Optional, Tuple

def test_standard_github_url() -> None:
    assert parse_github_url("https://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("http://github.com/user/repo") == ("user", "repo")
    assert parse_github_url("https://www.github.com/user/repo") == ("user", "repo")

def test_github_url_with_git_extension() -> None:
    assert parse_github_url("https://github.com/user/repo.git") == ("user", "repo")
    assert parse_github_url("https://github.com/user/repo.git/") == ("user", "repo")

def test_invalid_github_url() -> None:
    assert parse_github_url("https://example.com/user/repo") is None
    assert parse_github_url("https://github.com/") is None
    assert parse_github_url("https://github.com/user") is None
    assert parse_github_url("https://github.com/user/repo/subdir") is None

def test_empty_input() -> None:
    assert parse_github_url("") is None
    assert parse_github_url("   ") is None

def test_edge_cases() -> None:
    assert parse_github_url("https://github.com//repo") is None
    assert parse_github_url("https://github.com/user//") is None
    assert parse_github_url("https://github.com/user/repo.git.git") == ("user", "repo")