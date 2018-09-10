def cumulative_sum(n):
    """
    This function takes an integer and computes the cumulative sum of 0 to
    that integer. For instance if n = 523 , it returns 5+2+3+0 = 10.
    """
    # Edge case checking
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return ((n%10) + cumulative_sum(n/10))
