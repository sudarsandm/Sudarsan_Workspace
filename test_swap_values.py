from swap_values import swap_values_by_add_subtract, swap_values_by_multiply_divide
import pytest

def test_swap_values_by_add_subtract():
    assert swap_values_by_add_subtract(3,4) == (4,3) 
    assert swap_values_by_add_subtract(3,3) == 0
    assert swap_values_by_add_subtract(3.5,4.6) == 0
    assert swap_values_by_add_subtract('a','b') == 0

def test_swap_values_by_multiply_divide():
    assert swap_values_by_add_subtract(3,4) == (4,3)
    assert swap_values_by_add_subtract(3,3) == 0
    assert swap_values_by_add_subtract(3.5,4.6) == 0
    assert swap_values_by_add_subtract('a','b') == 0
