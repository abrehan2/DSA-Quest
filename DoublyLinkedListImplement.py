class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data) -> None:
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_start(data)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def delete_at_start(self) -> None:
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self) -> None:
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.next is None:
            self.head = None
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.prev.next = None

    def display(self) -> None:
        if self.head is None:
            raise Exception("Linked list is empty")

        itr = self.head
        listStr = ""

        while itr:
            listStr += str(itr.data) + " --> "
            itr = itr.next

        print(listStr)

# INSTANCES:
obj = Linked_list()
obj.insert_at_start(3)
obj.insert_at_end(5)
obj.insert_at_start(10)
obj.delete_at_start()
obj.delete_at_end()
obj.delete_at_end()
obj.display()
