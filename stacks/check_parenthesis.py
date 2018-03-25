from Stack import Stack
def check_parenthesis(s):
    """
    This function checks if '{','[','(',')',']','}' are available in a 
    matching combination pair using stack.
    """
    # Edge case check to see if there are odd number of parenthesis.
    if len(s)%2 != 0:
        return False
    
    stack = Stack()
    opening = set('([{')
    matches = set([('(',')'),('{','}'),('[',']')])

    for i in s:
        if i in opening:
            stack.push(i)
        elif stack.size() == 0:
            return False
        else:
            item = stack.pop()
            if (item,i) not in matches:
                return False
    return stack.size() == 0
