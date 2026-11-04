def test_empty_string():
    assert not validate_tags("", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("", {"tag1", "tag2", "tag3"})[1] == "Input string is empty"

def test_single_tag():
    assert validate_tags("tag1", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("tag1", {"tag1", "tag2", "tag3"})[1] == ""

def test_multiple_tags():
    assert validate_tags("tag1 | tag2 | tag3", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("tag1 | tag2 | tag3", {"tag1", "tag2", "tag3"})[1] == ""

def test_too_few_tags():
    assert not validate_tags("tag1", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("tag1", {"tag1", "tag2", "tag3"})[1] == "Number of tags is not between 1 and 3"

def test_too_many_tags():
    assert not validate_tags("tag1 | tag2 | tag3 | tag4", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("tag1 | tag2 | tag3 | tag4", {"tag1", "tag2", "tag3"})[1] == "Number of tags is not between 1 and 3"

def test_invalid_tag():
    assert not validate_tags("tag1 | invalid_tag", {"tag1", "tag2", "tag3"})[0]
    assert validate_tags("tag1 | invalid_tag", {"tag1", "tag2", "tag3"})[1] == "One or more tags are not in the valid tag set"

def test_valid_tag_set_empty():
    assert not validate_tags("tag1", set()) [0]
    assert validate_tags("tag1", set()) [1] == "One or more tags are not in the valid tag set"