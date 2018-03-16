from is_anagram import is_anagram
import pytest

def test_is_anagram():
    result = is_anagram('public relations','crap built on lies')
    assert result == True
    new_result = is_anagram('clint eastwood', 'old west action')
    assert new_result == True
