class MinStack:

    def __init__(self):
        self._stack = []
        self._min = self._top = None
        self._minstack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min is None:
            self._min = val
        if val < self._min:
            self._minstack.append(val)
            self._min = val
        else:
            self._minstack.append(self._min)
        self._top = val

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._minstack.pop()
        self._min = self._minstack[-1] if self._minstack else None
        self._top = self._stack[-1] if self._stack else None

    def top(self) -> int:
        return self._top

    def getMin(self) -> int:
        return self._min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(0)
# obj.push(1)
# obj.push(0)
# param_4 = obj.getMin()
# param_3 = obj.top()
