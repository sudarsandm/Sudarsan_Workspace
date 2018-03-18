def compress(s):
    """
    Compress a string on the basis of number of characters being repeated.
    For instance "AABBB" should compress to "A2B3".
    """
    # Edge case checking
    if len(s) == 0:
        return 0
    
    # Another Edge case check 
    if len(s) == 1:
        return s + '1'
    
    s = s.strip().rstrip()
    d = {}

    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    ret = ""
        
    for i in sorted(d.keys()):
        ret = ret + i + str(d[i])

    return ret
