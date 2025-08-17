# linearArray 不實作 ,因為需要在 Array 上搬移資料

class QueueWithCircularArray:
    def __init__(self, maxSize=10):
        self.array = [None] * maxSize
        self.maxSize = maxSize
        self.front = 0
        self.rear = 0

    def add(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.maxSize
        print(self.array)

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        self.array[self.front] = None
        self.front = (self.front + 1) % self.maxSize
        print(self.array)

    def isFull(self):
        return (self.rear + 1) % self.maxSize == self.front

    def isEmpty(self):
        return self.rear == self.front


queueInstance = QueueWithCircularArray()

queueInstance.delete()
queueInstance.add(1)
queueInstance.add(2)
queueInstance.add(3)
queueInstance.delete()
queueInstance.delete()
queueInstance.add(4)
queueInstance.delete()
queueInstance.delete()
queueInstance.delete()
queueInstance.add(5)
