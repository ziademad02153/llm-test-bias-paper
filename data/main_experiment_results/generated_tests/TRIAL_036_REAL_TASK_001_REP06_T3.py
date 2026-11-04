def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_with_www_and_git_extension():
    assert parse_github_url("https://www.github.com/owner/repo.git") == ("owner", "repo")

def test_http_url():
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

def test_invalid_url():
    assert parse_github_url("https://example.com/owner/repo") is None

def test_empty_input():
    assert parse_github_url("") is None

def test_malformed_url():
    assert parse_github_url("github.com/owner") is None