def finder(arr1,arr2):
    """
    This function finds the missing element between two arrays having same 
    values except for one
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
