def reverse_using_temp(s):
    """
    This module uses a temporary variable to reverse the sentence.
    """
    # Edge case check
    if len(s) == 0:
        return 0
    #stripping the leading and trailing white spaces and split into words
    words = s.strip().rstrip().split()

    length = int(len(words)/2)
    i = 0

    while i < length:
        temp = words[i]
        words[i] = words[len(words) -1 - i]
        words[len(words) -1 -i] = temp
        i += 1

    return " ".join(words)


