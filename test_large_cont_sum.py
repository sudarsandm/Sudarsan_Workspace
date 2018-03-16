from large_cont_sum import large_cont_sum
import pytest

def test_large_cont_sum():
    assert large_cont_sum([1,2,4,-3]) == 7
    assert large_cont_sum([]) == 0
    assert large_cont_sum([3]) == 3
    assert large_cont_sum([-1,2,3,-4]) == 5
