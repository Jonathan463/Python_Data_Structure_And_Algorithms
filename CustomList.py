class CustomList:
    def __init__(self):
        self.capacity = 4  # initial size of array
        self.size = 0      # number of elements in list
        self.array = [None] * self.capacity

    def __len__(self):
        return self.size

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.array[self.size] = value
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def remove(self, index):
        if 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError("Index out of bounds")

    def clear(self):
        self.size = 0


if __name__ == "__main__":
    lst = CustomList()
    lst.capacity = 5
    lst.append(3)
    lst.get(0)