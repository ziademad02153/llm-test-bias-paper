Here is a suite of comprehensive unit tests for the `validate_tags` function based on its specification:

```python
def test_empty_tags_string():
    valid, msg = validate_tags("", {"python", "api", "coding"})
    assert not valid
    assert "Non-empty string required" in msg

def test_too_many_tags():
    valid, msg = validate_tags("python|api|coding|test", {"python", "api", "coding", "test"})
    assert not valid
    assert "at most 3 non-empty tags" in msg

def test_invalid_tag():
    valid, msg = validate_tags("python|invalid", {"python", "api", "coding"})
    assert not valid
    assert "not in valid tag set" in msg.lower()

def test_valid_tags():
    valid, msg = validate_tags("python|api", {"python", "api", "coding"})
    assert valid
    assert msg == ""

def test_empty_tag_in_middle():
    valid, msg = validate_tags("python||api", {"python", "api", "coding"})
    assert not valid
    assert "non-empty tags" in msg.lower()

def test_single_valid_tag():
    valid, msg = validate_tags("python", {"python", "api", "coding"})
    assert valid
    assert msg == ""
```

These tests cover:
1. Empty input string (rule 1)
2. Too many tags (rule 2 upper bound)
3. Invalid tag presence (rule 3)
4. Valid case with multiple tags
5. Empty tag in middle of string (rule 2)
6. Valid single tag case (rule 2 lower bound)

All tests use simple assert statements and verify both the boolean result and error messages where applicable. The tests are independent and cover all specified rules without reimplementing the function.