from wordle_ql2581 import wordle_ql2581

# tests/test_wordle.py

import pytest
from wordle_ql2581.wordle_ql2581 import validate_guess, check_guess

def test_validate_guess():
    """
    Test the validate_guess function with valid and invalid inputs.
    """
    # Valid guess
    assert validate_guess("apple") is True

    # Invalid guesses
    assert validate_guess("app1e") is False   # contains a number
    assert validate_guess("AppLe") is False   # contains uppercase letters
    assert validate_guess("app") is False     # too short

def test_check_guess():
    """
    Test the check_guess function to ensure color hints are correct.
    """
    # Partial match example
    result1 = check_guess("apple", "apron")
    expected1 = [('a', 'green'), ('p', 'green'), ('r', 'gray'), ('o', 'gray'), ('n', 'gray')]
    assert result1 == expected1

    # Exact match example
    result2 = check_guess("reach", "reach")
    expected2 = [('r', 'green'), ('e', 'green'), ('a', 'green'), ('c', 'green'), ('h', 'green')]
    assert result2 == expected2
