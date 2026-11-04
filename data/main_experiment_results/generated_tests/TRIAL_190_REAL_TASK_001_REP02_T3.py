# Test standard GitHub URL with https
def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with http
def test_http_url():
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with www prefix
def test_www_prefix_url():
    assert parse_github_url("https://www.github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with .git extension
def test_git_extension_url():
    assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")

# Test invalid GitHub URL
def test_invalid_url():
    assert parse_github_url("https://github.com/owner") is None

# Test empty input
def test_empty_input():
    assert parse_github_url("") is None