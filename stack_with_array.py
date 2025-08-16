class StackWithArray:
    def __init__(self, maxSize=3):
        self.array = []
        self.maxSize = maxSize

    def push(self, item):
        if self.isFull():
            print("stack is full")
            return None
        self.array.append(item)
        print(self.array)
        return item

    def pop(self):
        if self.isEmpty():
            print("nothing in stack")
            return None
        item = self.array.pop()
        print(self.array)
        return item

    def top(self):
        if self.isEmpty():
            print("peek is not exist")
            return None
        print(self.array[-1])
        return self.array[-1]

    def isEmpty(self):
        return len(self.array) == 0

    def isFull(self):
        return len(self.array) == self.maxSize



stackInstance = StackWithArray()

stackInstance.pop()
stackInstance.push(1)
stackInstance.push(2)
stackInstance.push(3)
stackInstance.push(4)
stackInstance.top()
stackInstance.pop()
stackInstance.pop()
stackInstance.pop()
stackInstance.pop()


