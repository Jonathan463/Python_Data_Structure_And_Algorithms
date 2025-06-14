class CustomQueue:
    def __init__(self):
        self.data = []
        self.head = 0

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        if self.head >= 50 and self.head >= len(self.data) // 2:
            self.clean_up()
        data = self.data[self.head]
        self.head += 1
        return data

    def enqueue(self, value):
        self.data.append(value)

    def is_empty(self):
        return len(self.data) == 0

    def clean_up(self):
        self.data = self.data[self.head:]
        self.head = 0


if __name__ == '__main__':
    customQueue = CustomQueue()
    customQueue.enqueue(3)
    customQueue.enqueue(4)
    customQueue.enqueue(5)
    print(customQueue.dequeue())
    print(customQueue.data)
    print(customQueue.dequeue())
    print(customQueue.data)
    print(customQueue.is_empty())
