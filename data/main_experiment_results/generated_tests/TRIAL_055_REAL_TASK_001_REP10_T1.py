from typing import Optional, Tuple

def test_standard_github_url() -> None:
    """Test standard GitHub URL."""
    url = "https://github.com/user/repo"
    expected_output = ("user", "repo")
    assert parse_github_url(url) == expected_output

def test_github_url_with_git_extension() -> None:
    """Test GitHub URL with.git extension."""
    url = "https://github.com/user/repo.git"
    expected_output = ("user", "repo")
    assert parse_github_url(url) == expected_output

def test_invalid_github_url() -> None:
    """Test invalid GitHub URL."""
    url = "https://example.com/user/repo"
    expected_output: Optional[Tuple[str, str]] = None
    assert parse_github_url(url) == expected_output

def test_empty_github_url() -> None:
    """Test empty GitHub URL."""
    url = ""
    expected_output: Optional[Tuple[str, str]] = None
    assert parse_github_url(url) == expected_output

def test_github_url_with_www_prefix() -> None:
    """Test GitHub URL with www prefix."""
    url = "https://www.github.com/user/repo"
    expected_output = ("user", "repo")
    assert parse_github_url(url) == expected_output

def test_github_url_with_http_prefix() -> None:
    """Test GitHub URL with http prefix."""
    url = "http://github.com/user/repo"
    expected_output = ("user", "repo")
    assert parse_github_url(url) == expected_output

def test_github_url_with_invalid_path() -> None:
    """Test GitHub URL with invalid path."""
    url = "https://github.com/user"
    expected_output: Optional[Tuple[str, str]] = None
    assert parse_github_url(url) == expected_output