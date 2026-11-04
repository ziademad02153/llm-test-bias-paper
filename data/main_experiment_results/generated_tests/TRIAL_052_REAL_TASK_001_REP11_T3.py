def test_standard_github_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_with_www_and_git_extension():
    assert parse_github_url("https://www.github.com/owner/repo.git") == ("owner", "repo")

def test_http_no_www():
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

def test_invalid_url_format():
    assert parse_github_url("https://gitlab.com/owner/repo") is None

def test_empty_string():
    assert parse_github_url("") is None

def test_missing_repo_part():
    assert parse_github_url("https://github.com/owner/") is None