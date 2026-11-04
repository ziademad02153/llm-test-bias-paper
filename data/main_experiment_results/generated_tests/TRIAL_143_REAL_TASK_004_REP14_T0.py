import unittest
from typing import Tuple, Set
from dataclasses import dataclass
from typing import Tuple, Set

@dataclass
class TestCaseResult:
    is_valid: bool
    error_message: str

def validate_tags(tags: str, valid_tag_set: Set[str]) -> Tuple[bool, str]:
    # function implementation not shown

def test_valid_tags():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_empty_string():
    tags = ""
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Input string is empty")

def test_less_than_one_tag():
    tags = "coding"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Must contain at least 1 and at most 3 non-empty tags")

def test_more_than_three_tags():
    tags = "coding | python | api | testing"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Must contain at least 1 and at most 3 non-empty tags")

def test_invalid_tag():
    tags = "coding | invalid | api"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Every tag must be present in valid_tag_set")

def test_valid_tag():
    tags = "coding | python | api"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_empty_valid_tag_set():
    tags = "coding | python | api"
    valid_tag_set = set()
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Every tag must be present in valid_tag_set")

def test_single_tag():
    tags = "coding"
    valid_tag_set = {"coding", "python", "api"}
    result = validate_tags(tags, valid_tag_set)
    assert result == (True, "")

def test_single_tag_empty_valid_tag_set():
    tags = "coding"
    valid_tag_set = set()
    result = validate_tags(tags, valid_tag_set)
    assert result == (False, "Every tag must be present in valid_tag_set")