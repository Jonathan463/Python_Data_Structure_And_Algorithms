class CustomQueue:
    def __init__(self):
        self.data = []
        self.head = 0

    def dequeue(self):
        if self.head >= len(self.data):
            raise ValueError("Queue is empty")
        data = self.data[self.head]
        self.head += 1
        return data

    def enqueue(self,value):
        self.data.append(value)


if __name__ == '__main__':
    customQueue = CustomQueue()
    customQueue.enqueue(3)
    customQueue.enqueue(4)
    customQueue.enqueue(5)
    print(customQueue.dequeue())
    print(customQueue.data)
    print(customQueue.dequeue())
    print(customQueue.data)