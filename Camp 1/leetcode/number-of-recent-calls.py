class RecentCounter:

    def __init__(self):
        self.left = 0
        self.right = 0
        self.arr = []
        

    def ping(self, t: int) -> int:
        if self.right == 0:
            self.arr.append(t)
            self.right += 1
            return 1
        self.right += 1
        self.arr.append(t)
        while self.left < self.right and self.arr[self.left] < t - 3000:
            self.left += 1
        return self.right - self.left


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)