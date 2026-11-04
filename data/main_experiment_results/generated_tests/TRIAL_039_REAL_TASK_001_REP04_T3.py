Here's a comprehensive suite of unit tests for the `parse_github_url` function based on its specification:

```python
# Test standard GitHub URLs
def test_standard_github_url():
    assert parse_github_url("https://github.com/owner/repo") == ("owner", "repo")
    assert parse_github_url("http://github.com/owner/repo") == ("owner", "repo")
    assert parse_github_url("https://www.github.com/owner/repo") == ("owner", "repo")

# Test with .git extension
def test_git_extension():
    assert parse_github_url("https://github.com/owner/repo.git") == ("owner", "repo")
    assert parse_github_url("http://github.com/owner/repo.git") == ("owner", "repo")

# Test invalid URLs
def test_invalid_urls():
    assert parse_github_url("https://gitlab.com/owner/repo") is None
    assert parse_github_url("not-a-url") is None
    assert parse_github_url("https://github.com/owner") is None
    assert parse_github_url("https://github.com/owner/repo/extra") is None

# Test edge cases
def test_edge_cases():
    assert parse_github_url("") is None
    assert parse_github_url("github.com/owner/repo") is None
    assert parse_github_url("https://api.github.com/repos/owner/repo") is None
```

This test suite covers:
1. Standard GitHub URL formats with different protocols and www prefix
2. URLs with .git extension
3. Clearly invalid URLs (non-GitHub, malformed, wrong path structure)
4. Edge cases (empty string, missing protocol, API URLs)
5. Cases that should return None according to the spec

All tests follow the specification without making assumptions about the implementation details.