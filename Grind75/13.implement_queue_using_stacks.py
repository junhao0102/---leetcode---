class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        return self.stack.pop(length - 1)

    def peek(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        if length == 0:
            return 0
        return self.stack[length - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

