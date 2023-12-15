class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.flips = defaultdict(int)
        self.allFlips = 0
        self.ones = 0
      

    def fix(self, idx: int) -> None:        
        self.ones += 1 if (self.flips[idx]+self.allFlips) % 2 == 0 else 0 
        self.flips[idx] += 1 if (self.flips[idx]+self.allFlips) % 2 == 0 else 0
        
    def unfix(self, idx: int) -> None:        
        self.ones -= 1 if (self.flips[idx]+self.allFlips) % 2 == 1 else 0 
        self.flips[idx] += 1 if (self.flips[idx]+self.allFlips) % 2 == 1 else 0
        

    def flip(self) -> None:
        self.allFlips += 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        string = ''
        for i in range(self.size):
            string += str((self.flips[i] + self.allFlips) % 2)
        return string

'''
00010

{
    3:1, 1:1
}
tf = 3
0 1

01
0
flips 2 
["Bitset","fix","flip","fix","flip","all","unfix","flip","one","unfix","count","toString"]
[[5],[3],[],[1],[],[],[0],[],[],[0],[],[]]

'''
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()