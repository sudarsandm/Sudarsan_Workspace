from sentence_reversal import reverse_using_temp
import pytest

def test_reverse_using_temp():
    assert reverse_using_temp("I was in tpt.") == "tpt. in was I"
    assert reverse_using_temp("") == 0
