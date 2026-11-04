def test_standard_https_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_standard_http_url():
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

def test_www_prefix_url():
    assert parse_github_url("https://www.github.com/owner/repo") == ("owner", "repo")

def test_url_with_git_extension():
    assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")

def test_invalid_url_non_github_domain():
    assert parse_github_url("https://gitlab.com/owner/repo") is None

def test_invalid_url_too_many_path_components():
    assert parse_github_url("https://github.com/owner/repo/extra") is None

def test_invalid_url_empty_path():
    assert parse_github_url("https://github.com") is None