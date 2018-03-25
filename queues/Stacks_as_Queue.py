class Stacks_Queue(object):
    """
    We are using two stacks in a pipeline to represent one queue.
    """
    def __init__(self):
        """
        This is the constructor method for this queue class.
        """
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        """
        This method is used to push data to the rear end of the queue.
        """
        self.instack.append(item)

    def dequeue(self):
        """
        This method is used to pop the first element which entered the 
        Queue. So we pop the instack elements to outstack so that the
        first member in the instack remains at top of outstack.
        """
        while self.instack:
            self.outstack.append(self.instack.pop())
        try:
            return self.outstack.pop()
        except IndexError as e:
            print("Queue is Empty")
