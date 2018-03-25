from Stack import Stack
def reverse_str(s):
    """
    This function uses an already implemented stack to reverse a string.
    """
    # Edge case check
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return s

    stack = Stack()
    
    for i in s:
        stack.push(i)

    reversed_list = []

    while stack.isEmpty() == False:
        reversed_list.append(stack.pop())

    return "".join(reversed_list)
