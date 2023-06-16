class Stack:
    def __init__(self, capacity: int):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity: int = capacity

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.capacity - 1

    def push(self, value) -> None:
        if self.is_full():
            print("Stack is full")
            return None
        self.top += 1
        self.stack[self.top] = value

    def pop(self) -> int | None:
        if self.is_empty():
            print("Stack is empty")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        return item

    def peek(self) -> int | None:
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def __repr__(self) -> str:
        return f"{self.stack}"


stack = Stack(4)
stack.push(3)
stack.push(2)
stack.push(3)
stack.push(4)
# stack.push(44)
print(stack)
print(stack.peek())
