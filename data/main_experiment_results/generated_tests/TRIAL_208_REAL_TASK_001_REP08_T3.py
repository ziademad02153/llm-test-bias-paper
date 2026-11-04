def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_www_and_git_extension():
    assert parse_github_url("https://www.github.com/owner/repo.git") == ("owner", "repo")

def test_http_no_www():
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

def test_invalid_url_missing_repo():
    assert parse_github_url("https://github.com/owner") is None

def test_empty_input():
    assert parse_github_url("") is None

def test_non_github_url():
    assert parse_github_url("https://gitlab.com/owner/repo") is None