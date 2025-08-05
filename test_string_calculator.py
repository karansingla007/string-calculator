import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("5") == 5

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newlines_between_numbers():
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert add("//;\n1;2;3") == 6

def test_custom_delimiter_pipe():
    assert add("//|\n1|2|3") == 6