class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link


class QueueWithLinkList:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, node):
        if self.rear == None:
            self.front = node
            self.rear = node
            print("front:" + str(self.front.value))
            print("rear:" + str(self.rear.value))

        else:
            self.rear.link = node
            self.rear = node
            print("front:" + str(self.front.value))
            print("rear:" + str(self.rear.value))

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        ptr = self.front
        self.front = self.front.link

        # 刪除最後一個 node 時，把 rear 也清空
        if self.front is None:
            self.rear = None
        print(ptr.value)
        return ptr

    def isEmpty(self):
        return self.rear == None

    def isFull(self):
        return False


queueInstance = QueueWithLinkList()

queueInstance.delete()
queueInstance.add(Node(1))
queueInstance.add(Node(2))
queueInstance.add(Node(3))
queueInstance.delete()
queueInstance.delete()
queueInstance.delete()
queueInstance.delete()
