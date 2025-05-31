import array


class CustomArray:
    #append
    #get
    #delete
    #clear
    def __init__(self, size=0):
        self.size = size
        # self.data = array.array("i")
        self.data = {}

    def get(self,index):
        return self.data[index]

    def append(self,value):
        self.data[self.size] = value
        self.size +=1
         # self.data.append(value)

    def clear(self):
        self.data = {}
        return

    def delete(self,index):
        for i in range(index, self.size-1):
            self.data[index] = self.data[index+1]
            index +=1
        del self.data[self.size-1]


if __name__ == '__main__':
    arr = CustomArray()
    arr.append(2)
    arr.append(5)
    arr.append(3)
    arr.append(1)
    arr.append(7)
    arr.append(9)
    print(arr.data.values())
    print(arr.delete(2))
    print(arr.data.values())
    arr.clear()
    print(arr.data.values())