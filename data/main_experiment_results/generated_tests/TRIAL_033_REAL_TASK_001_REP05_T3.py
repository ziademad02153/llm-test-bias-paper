# Test standard GitHub URL with https
def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with http and www prefix
def test_http_www_url():
    assert parse_github_url("http://www.github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with .git extension
def test_git_extension_url():
    assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")

# Test invalid GitHub URL (missing owner/repo)
def test_invalid_url_missing_parts():
    assert parse_github_url("https://github.com") is None

# Test empty input
def test_empty_input():
    assert parse_github_url("") is None

# Test non-GitHub URL
def test_non_github_url():
    assert parse_github_url("https://gitlab.com/owner/repo") is None