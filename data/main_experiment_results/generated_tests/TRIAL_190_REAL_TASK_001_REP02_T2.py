def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_http_url_with_www_and_git():
    assert parse_github_url("http://www.github.com/owner/repo.git") == ("owner", "repo")

def test_invalid_domain():
    assert parse_github_url("https://gitlab.com/owner/repo") is None

def test_invalid_path_format():
    assert parse_github_url("https://github.com/owner") is None
    assert parse_github_url("https://github.com/owner/repo/extra") is None

def test_empty_url():
    assert parse_github_url("") is None

def test_url_with_trailing_slash():
    assert parse_github_url("https://github.com/owner/repo/") == ("owner", "repo")