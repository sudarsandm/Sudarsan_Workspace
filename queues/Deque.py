class Deque(object):
    """
    Deque is double ended Queue in which we can add element at the front
    end and also at the rear end. Delection can also happen at both the 
    ends.
    """
    def __init__(self):
        """
        This is the constructor Method for this class.
        """
        self.items = []

    def addFront(self,item):
        """
        This method adds element at the front end.
        """
        self.items.append(item)

    def addRear(self,item):
        """
        This method is equivalent to the enqueue method in a standard 
        Queue class. We add element at the rear end.
        """
        self.items.insert(0,item)

    def removeFront(self):
        """
        This method removes element at the front end.
        """
        try:
            self.items.pop()
        except IndexError as e:
            print("Deque is empty")

    def removeRear(self):
        """
        This method removes element at the rear end.
        """
        try:
            self.items.pop(0)
        except IndexError as e:
            print("Deque is empty")

    def isEmpty(self):
        """
        This method checks if a Deque is empty.
        """
        return self.items == []

    def size(self):
        """
        This method returns the size of the element.
        """
        return len(self.items)
