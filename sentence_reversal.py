def reverse_list(arr):
    """
    This function reverses a list using a temp variable.
    This is defined to avoid code repetition.
    """
    length = int(len(arr)/2)
    i = 0
    
    while i < length:
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp
        i += 1
    return arr


def reverse_using_temp(s):
    """
    This module uses a temporary variable to reverse the sentence.
    """
    # Edge case check
    if len(s) == 0:
        return 0
    #stripping the leading and trailing white spaces and split into words
    words = s.strip().rstrip().split()

    # calling out the reverse_list function to reverse the words list
    words = reverse_list(words)

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
        # To check if we are in word boundary
        if s[i] not in space:
            word_start = i
            # increment i until we hit a space or word boundary
            while i < length and s[i] not in space:
                i += 1
            # once the word boundary is reached append it words
            words.append(s[word_start:i])
        i += 1

    # calling out the reverse_list function to reverse the words list
    words = reverse_list(words)
    
    return " ".join(words)
