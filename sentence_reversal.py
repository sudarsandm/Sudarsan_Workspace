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

def reverse_using_whitespace(s):
    """
    We will look for word boundaries in terms of space in the sentence.
    """
    # Edge case check
    if len(s) == 0:
        return 0

    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i
            # increment i until we hit a space or word boundary
            while i < length and s[i] not in space:
                i += 1
            # once the word boundary is reached append it words
            words.append(s[word_start:i])
        i += 1

    j = 0
    length = len(words)

    # This code block is used to reverse the words
    while j < int(length/2):
        temp = words[j]
        words[j] = words[length - 1 - j]
        words[length - 1 - j] = temp
        j += 1
    
    return " ".join(words)
