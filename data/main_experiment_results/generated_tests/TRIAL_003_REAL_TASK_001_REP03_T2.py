def test_standard_github_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")

def test_github_url_with_www():
    assert parse_github_url("https://www.github.com/owner/repo") == ("owner", "repo")

def test_github_url_with_git_extension():
    assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")

def test_invalid_github_url():
    assert parse_github_url("https://gitlab.com/owner/repo") is None

def test_invalid_path_format():
    assert parse_github_url("https://github.com/owner") is None

def test_empty_url():
    assert parse_github_url("") is None