class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.front = 0
        self.rear = 0
        self.length = k
        
    def enQueue(self, value: int) -> bool:
        if self.arr[self.rear] != -1:
            return False
        self.arr[self.rear] = value
        self.rear += 1
        self.rear %= self.length
        return True

    def deQueue(self) -> bool:
        if self.arr[self.front] == -1:
            return False
        self.arr[self.front] = -1
        self.front += 1
        self.front %= self.length
        return True

    def Front(self) -> int:
        return self.arr[self.front]

    def Rear(self) -> int:
        return self.arr[(self.rear-1)%self.length]

    def isEmpty(self) -> bool:
        return self.arr[self.front] == -1

    def isFull(self) -> bool:
        return self.front == self.rear and self.arr[self.front] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()