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

    def insert_values(self, values):
        self.head = None

        for data in values:
            self.insert_at_end(data)

    def get_linked_list_length(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        count = 0
        while itr:
            count = count + 1
            itr = itr.next

        return count
    
    def remove_at(self, index):

          if index < 0 or index > self.get_linked_list_length():
              raise Exception("Invalid index given")
  
          if index == 0:
              self.head = self.head.next
              return
  
          count = 0
          itr = self.head
  
          while itr:
              if count == index-1:
                  itr.next = itr.next.next
                  break
  
              itr = itr.nxt
              count = count + 1


    def insert_at(self, index, data):
        if index < 0 or index > self.get_linked_list_length():
            raise Exception("Invalid index given")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


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