class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


class MyStack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.enqueue(x)
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        if self.q1.isEmpty():
            return None
        return self.q1.dequeue()

    def top(self):
        """
        :rtype: int
        """
        if self.q1.isEmpty():
            return None
        return self.q1.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.isEmpty()


Stack = MyStack()
Stack.push(1)
Stack.push(2)

print(Stack.top())  # return 2
print(Stack.pop())  # return 2
print(Stack.empty())  # return False

print(Stack.top())  # return 1
print(Stack.pop())  # return 1
print(Stack.empty())  # return True
