class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data) -> None:
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_start(data)

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data) -> None:
        self.head = None

        for value in data:
            self.insert_at_start(value)

    def get_length(self) -> int:
        if self.head is None:
            raise Exception("Linked list is empty!")

        itr = self.head
        count = 0

        while itr:
            count = count + 1
            itr = itr.next

        print("Length:", count)
        return count

    def remove_at(self, index) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count = count + 1

    def update_at(self, index, value) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head.data = value
            return

        itr = self.head
        count = 0

        while itr:
            if count == index:
                itr.data = value
                break

            itr = itr.next
            count = count + 1

    def insert_at(self, index, value) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(value)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break

            itr = itr.next
            count = count + 1

    def display(self) -> None:
        if self.head is None:
            raise Exception("Linked list is empty!")

        itr = self.head
        listStr = ""

        while itr:
            listStr += str(itr.data) + " --> "
            itr = itr.next

        print(listStr)


# INSTANCES:
obj = LinkedList()
obj.insert_at_start(3)
obj.insert_at_start(5)
obj.insert_at_end(8)
obj.insert_at_end(10)
obj.insert_values([5, 6, 7])
obj.get_length()
obj.remove_at(2)
obj.update_at(0, 11)
obj.update_at(1, 12)
obj.update_at(2, 13)
obj.insert_at(0, 5)
obj.insert_at(1, 20)
obj.display()
