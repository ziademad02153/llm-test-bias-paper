# Test standard GitHub URL with https and .git extension
assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")

# Test standard GitHub URL with http and no .git extension
assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")

# Test GitHub URL with www prefix
assert parse_github_url("https://www.github.com/owner/repo") == ("owner", "repo")

# Test invalid GitHub URL (missing owner/repo)
assert parse_github_url("https://github.com/") is None

# Test empty input
assert parse_github_url("") is None

# Test non-GitHub URL
assert parse_github_url("https://example.com/owner/repo") is None