class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link


class StackWithLinkList:
    def __init__(self):
        self.top = None

    def push(self, node):
        node.link = self.top
        self.top = node
        print(self.top.value)

    def pop(self):
        if self.top == None:
            print("stack is empty")
            return
        ptr = self.top
        self.top = self.top.link
        return ptr.value

    def peek(self):
        if self.top:
            print(self.top.value)
            return self.top.value
        return None

    def isFull(self):
        return False

    def isEmpty(self):
        return self.top == None

stackInstance = StackWithLinkList()
stackInstance.pop()
stackInstance.push(Node(1))
stackInstance.push(Node(2))
stackInstance.push(Node(3))
stackInstance.peek()
stackInstance.pop()
stackInstance.pop()
stackInstance.peek()
stackInstance.pop()
stackInstance.pop()

