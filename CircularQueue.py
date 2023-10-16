class Node:
   def __init__(self, val, next, prev) -> None:
       self.val = val
       self.next = next
       self.prev = prev

class MyCircularQueue:
    def __init__(self, k: int) -> None:
        self.space = k
        self.left = Node(0, None, None)
        self.right = Node(0, None, self.left)
        self.left.next = self.right  
    
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        curr = Node(val, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True
    
    def deQueue(self) -> bool:
        if self.isFull(): return False
        self.left.next = self.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True
    
    def isEmpty(self) -> bool:
        return self.left.next == self.right
    
    def isFull(self) -> bool:
        return self.space == 0
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.left.next.val
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.right.prev.val
        