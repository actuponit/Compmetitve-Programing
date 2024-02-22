class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        mini = min(val, self.arr[-1][0]) if len(self.arr) > 0 else val
        self.arr.append((mini, val)) 

    def pop(self) -> None:
        self.arr.pop() 

    def top(self) -> int:
        (_, top) = self.arr[-1]
        return top

    def getMin(self) -> int:
        (mini, _) = self.arr[-1]
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()