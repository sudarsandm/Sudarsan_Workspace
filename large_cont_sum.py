def large_cont_sum(arr):
    """
    This function computes the largest continous sum for a given array.
    """
    # Edge case checking
    if len(arr) == 0:
        return 0 
    elif len(arr) == 1:
        return arr[0]

    # This block of code is to select non-negative number as max_sum 
    for i in arr:
        if i < 0:
            continue
        else:
            max_sum = cont_sum = i
            arr.remove(i)
            break
    # We will proceed with the rest of the array
    for num in arr:
        cont_sum = max_sum + num
        max_sum = max(max_sum, cont_sum)

    return max_sum
