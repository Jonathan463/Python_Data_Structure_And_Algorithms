from CustomArray import CustomArray


class Stack(CustomArray):
    def __init__(self):
        super().__init__()

    def enqueu(self,value):
        self.append(value)


    def dequeue(self):
        return

        
if __name__ == '__main__':
    stack = Stack()
    stack.enqueu(3)
    stack.enqueu(4)
    stack.enqueu(7)
    print(stack.data.values())