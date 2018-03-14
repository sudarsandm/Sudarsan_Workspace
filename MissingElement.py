from collections import defaultdict
def finder(arr1,arr2):
    """
    This function finds the missing element between two arrays having same 
    values except for one. This approach uses count method associated with
    lists data structure in python.
    """
    miss_item = 0
    for item in arr1:
        if (arr2.count(item) == 0):
            miss_item = item
        else:
            continue
      
    if (miss_item == 0):
        return None 
    else:
        return miss_item
def finder_dict(arr1, arr2):
    """
    This function finds the missing element using default dict from
    collections module. We can also use an empty dictionary to use 
    it for finding the missing element.
    """
    # create an empty dictionary which can hold integer values
    numbers = defaultdict(int)

    # Populate the dictionary with occurence of each element
    for i in arr2:
        numbers[i] += 1
    # isolate the element by comparing the dictionary with arr1

    for i in arr1:
        if i in numbers:
            numbers[i] -= 1
        else:
            return i
    
