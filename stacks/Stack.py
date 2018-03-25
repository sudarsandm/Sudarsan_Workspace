class Stack(object):
    """
    This is a Stack class implementation. The basic operations on a stack
    or also implemented as it's method. The stack operates on the basic
    principle of 'Last In First Out'(LIFO).
    """
    def __init__(self):
        """
        This is the constructor class for the stack.
        """
        self.items = []

    def push(self,item):
        """
        This method is used to add an element to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        This method is used to delete an element from the top of the stack.
        """
        try:
            return self.items.pop() 
        except:
            print("Stack is empty")
            raise

    def isEmpty(self):
        """
        This is a method which returns a boolean True if stack is empty.
        """
        return self.items == [] 

    def peek(self):
        """
        This function returns the item in the top of the stack but does not
        remove it from stack.
        """
        return self.items[len(self.items)-1] 

    def size(self):
        """
        Length of the stack or number of elements in the stack
        """
        return len(self.items)
