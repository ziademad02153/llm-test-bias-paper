Here's a comprehensive set of unit tests for the `validate_tags` function:

```python
def test_empty_input():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("", valid_tags)
    assert not is_valid
    assert msg == "Input string is empty"

def test_too_many_tags():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python|api|coding|extra", valid_tags)
    assert not is_valid
    assert msg == "Number of tags is not between 1 and 3"

def test_invalid_tag():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python|invalid", valid_tags)
    assert not is_valid
    assert msg == "One or more tags are not in the valid tag set"

def test_valid_single_tag():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python", valid_tags)
    assert is_valid
    assert msg == ""

def test_valid_multiple_tags():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python|api|coding", valid_tags)
    assert is_valid
    assert msg == ""

def test_whitespace_in_tags():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags(" python |  api  ", valid_tags)
    assert not is_valid  # Because whitespace isn't stripped in implementation
    assert msg == "One or more tags are not in the valid tag set"
```

Note: The last test (`test_whitespace_in_tags`) reveals a potential issue with the implementation - it doesn't strip whitespace from tags before validation. This is left as-is to match the exact specification, but in a real-world scenario, you might want to either:
1. Update the implementation to handle whitespace, or
2. Explicitly document that whitespace is significant in tags