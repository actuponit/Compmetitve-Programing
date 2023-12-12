class OrderedStream:

    def __init__(self, n: int):
        self.arr = ['']*n
        self.pos = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        chunk = []
        if idKey-1 == self.pos:
            while self.pos < len(self.arr) and self.arr[self.pos] != '':
                chunk.append(self.arr[self.pos])
                self.pos += 1
        return chunk

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)