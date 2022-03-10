class Queue:
    """
    A basic implementation of a Queue
    """

    def __init__(self):
        """
        Start with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Provide a string representation for this object.
        """
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result
