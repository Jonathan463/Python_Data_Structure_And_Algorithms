class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tail pointer

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_record = Node(data)
        if self.is_empty():
            self.head = self.tail = new_record
        else:
            self.tail.next = new_record
            self.tail = new_record

    def prepend(self, data):
        new_record = Node(data)
        if self.is_empty():
            self.head = self.tail = new_record
        else:
            new_record.next = self.head
            self.head = new_record

    def delete(self, position):
        if self.is_empty():
            raise ValueError("Cannot delete an item from an empty linkedList")
        else:
            current = self.head
            prev = None
            for i in range(1,position):
                prev = current
                current = current.next
            prev.next = current.next

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display(self):
        print("LinkedList:", self.to_list())

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(2)
    linkedList.append(4)
    linkedList.append(6)
    linkedList.append(7)
    linkedList.append(9)
    linkedList.display()
    linkedList.delete(2)
    linkedList.display()
