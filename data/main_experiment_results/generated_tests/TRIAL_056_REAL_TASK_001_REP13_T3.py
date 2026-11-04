def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_http_url_with_www_and_git_extension():
    assert parse_github_url("http://www.github.com/owner/repo.git") == ("owner", "repo")

def test_invalid_url_missing_owner():
    assert parse_github_url("https://github.com/repo") is None

def test_empty_input():
    assert parse_github_url("") is None

def test_non_github_domain():
    assert parse_github_url("https://gitlab.com/owner/repo") is None

def test_url_with_trailing_slash():
    assert parse_github_url("https://github.com/owner/repo/") == ("owner", "repo")