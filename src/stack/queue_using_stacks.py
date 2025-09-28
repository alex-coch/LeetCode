class MyQueue:

    def __init__(self):
        self.stack_main = []
        self.stack_add = []

    def push(self, x: int) -> None:
        while self.stack_main:
           self.stack_add.append(self.stack_main.pop())
        self.stack_main.append(x)
        while self.stack_add:
           self.stack_main.append(self.stack_add.pop())

    def pop(self) -> int:
        return self.stack_main.pop()

    def peek(self) -> int:
        return self.stack_main[-1]

    def empty(self) -> bool:
        return len(self.stack_main) == 0
