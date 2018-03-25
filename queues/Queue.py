class Queue(object):
    """
    This is the implementation of a Queue class. This data structure follows 
    the First In First Out principle. The first one added to this data 
    structure is the first one to be popped out.
    """
    def __init__(self):
        """
        This is the constructor method for this Queue class.
        """
        self.items = []

    def enqueue(self, item):
        """
        This method pushes the element to this Queue data structure at the 
        rear end.
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        This method pops the element at the front end.
        """
        try:
            return self.items.pop()
        except IndexError as e:
            print("Queue is Empty")

    def isEmpty(self):
        """
        This method checks if the Queue is Empty.
        """
        return self.items == []

    def size(self):
        """
        This method returns the length of the Queue or number if elements in
        the queue.
        """
        return len(self.items)
