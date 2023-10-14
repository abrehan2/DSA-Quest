class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class Linked_list:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert_at_head(self, val) -> None:
        node = Node(val)

        if self.size == 0:
            node.next = self.head
            self.head = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def insert_at_tail(self, val) -> None:
        if self.head is None:
            self.insert_at_head(val)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(val)
        itr.next = node
        node.prev = itr
        self.size += 1

    def get(self, index) -> int:
        if index < 0 or index > self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val

    def insert_at(self, index, val) -> None:
        if index < 0 or index > self.size:
            return -1

        if index == 0:
            self.insert_at_head(val)
            return

        if index == self.size:
            self.insert_at_tail(val)
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next

        node = Node(val)

        node.next = itr.next
        node.prev = itr
        itr.next = node
        node.next.prev = node

    def remove_at(self, index) -> None:
        if index < 0 or index > self.size:
            return -1

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        for i in range(index-1):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1


# INSTANCES:
obj = Linked_list()
obj.insert_at_head(3)  # 0
obj.insert_at_head(4)  # 1
obj.insert_at_tail(5)  # 3
obj.insert_at(2, 10)  # 2
# obj.remove_at(2)
# obj.remove_at(0)
obj.remove_at(3)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))

