import sorting_algorithms as sort
import pytest

@pytest.mark.parametrize("list1, sorted_list",
                        [ 
                            ([9,0,3,7,1,6], sorted([9,0,3,7,1,6]))
                        ]
                        )
def test_bubble_sort(list1, sorted_list):
    assert sort.bubble_sort(list1) == sorted_list

@pytest.mark.parametrize("list1, sorted_list",
                        [
                             ([2,9,0,5,8], sorted([2,9,0,5,8]))
                        ]
                        )
def test_insertion_sort(list1, sorted_list):
        assert sort.insertion_sort(list1) == sorted_list

@pytest.mark.parametrize("list1, sorted_list",
                        [
                            ([8,10,3,9,0,1,4], sorted([8,10,3,9,0,1,4]))
                        ]
                        )
def test_selection_sort(list1, sorted_list):
        assert sort.selection_sort(list1) == sorted_list
