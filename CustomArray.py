import array


class CustomArray:
    def __init__(self, size=0):
        self.size = size
        self.data = array.array("i")

    def get(self,index):
        return self.data[index]

    def append(self,value):
        self.data.append(value)

if __name__ == '__main__':
    arr = CustomArray()
    arr.append(2)
    print(arr.get(0))