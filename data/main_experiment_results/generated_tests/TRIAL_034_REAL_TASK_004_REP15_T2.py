Here's a comprehensive suite of unit tests for the `validate_tags` function:

```python
def test_empty_input():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("", valid_tags)
    assert not is_valid
    assert msg == "Input string is empty"

def test_single_valid_tag():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python", valid_tags)
    assert is_valid
    assert msg == ""

def test_max_tags():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags("python|api|coding", valid_tags)
    assert is_valid
    assert msg == ""

def test_too_many_tags():
    valid_tags = {"python", "api", "coding", "test"}
    is_valid, msg = validate_tags("python|api|coding|test", valid_tags)
    assert not is_valid
    assert msg == "Number of tags is not between 1 and 3"

def test_invalid_tag():
    valid_tags = {"python", "api"}
    is_valid, msg = validate_tags("python|ruby", valid_tags)
    assert not is_valid
    assert msg == "One or more tags are not in the valid tag set"

def test_whitespace_handling():
    valid_tags = {"python", "api", "coding"}
    is_valid, msg = validate_tags(" python |  api  ", valid_tags)
    assert is_valid
    assert msg == ""