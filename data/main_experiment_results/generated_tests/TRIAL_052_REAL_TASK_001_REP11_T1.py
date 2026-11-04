from typing import Optional, Tuple

def test_standard_github_url() -> None:
    """Test standard GitHub URL."""
    url = "https://github.com/user/repo"
    assert parse_github_url(url) == ("user", "repo")

def test_github_url_with_git_extension() -> None:
    """Test GitHub URL with.git extension."""
    url = "https://github.com/user/repo.git"
    assert parse_github_url(url) == ("user", "repo")

def test_invalid_github_url() -> None:
    """Test invalid GitHub URL."""
    url = "https://example.com/user/repo"
    assert parse_github_url(url) is None

def test_empty_github_url() -> None:
    """Test empty GitHub URL."""
    url = ""
    assert parse_github_url(url) is None

def test_github_url_with_www_prefix() -> None:
    """Test GitHub URL with www prefix."""
    url = "https://www.github.com/user/repo"
    assert parse_github_url(url) == ("user", "repo")

def test_github_url_with_http_prefix() -> None:
    """Test GitHub URL with http prefix."""
    url = "http://github.com/user/repo"
    assert parse_github_url(url) == ("user", "repo")

def test_github_url_with_invalid_path() -> None:
    """Test GitHub URL with invalid path."""
    url = "https://github.com/user"
    assert parse_github_url(url) is None

def test_github_url_with_trailing_slash() -> None:
    """Test GitHub URL with trailing slash."""
    url = "https://github.com/user/repo/"
    assert parse_github_url(url) == ("user", "repo")