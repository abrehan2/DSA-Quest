# IMPORTS -
from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, data) -> None:
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self) -> bool:
        return len(self.container) == 0

    def size(self) -> int:
        return len(self.container)


# INSTANCES -
obj = Stack()
print(obj.is_empty())
obj.push(100)
print(obj.is_empty())
print(obj.peek())
