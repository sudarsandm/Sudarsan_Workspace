from sentence_reversal import reverse_using_temp, reverse_using_whitespace
import pytest

def test_reverse_using_temp():
    assert reverse_using_temp("I was in tpt.") == "tpt. in was I"
    assert reverse_using_temp("") == 0

def test_reverse_using_whitespace():
    assert reverse_using_whitespace("Twinkle Twinkle Little Star") == "Star" \
            + " Little Twinkle Twinkle"
    assert reverse_using_whitespace("") == 0
