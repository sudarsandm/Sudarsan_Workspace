from pair_sum import pair_sum
import pytest

def test_pair_sum():
    result = pair_sum([3,1,2,2], 4)
    assert result == [(1,3),(2,2)]
