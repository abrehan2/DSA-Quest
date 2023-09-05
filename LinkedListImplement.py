class Node:
    def __init__(self, data: None, next: None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listStr = ""

        while itr:
            listStr += str(itr.data) + "-->"
            itr = itr.next

        print(listStr)

if __name__ == "__main__":
   linked_list_object = Linked_list()
   linked_list_object.insert_at_begining(1)
   linked_list_object.insert_at_begining(2)
   linked_list_object.insert_at_begining(3)
   linked_list_object.print()