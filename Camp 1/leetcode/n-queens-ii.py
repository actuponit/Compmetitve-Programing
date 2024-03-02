class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(path, idx):
            if path == n:
                self.ans += 1
                return
            for i in range(n):
                if i in mp['col'] or i+idx in mp['ld'] or i-idx in mp['rd']:
                    continue
                # path.append((idx, i))
                mp['col'].add(i)
                mp['ld'].add(i+idx)
                mp['rd'].add(i-idx)
                backtrack(path+1, idx+1)
                mp['col'].remove(i)
                mp['ld'].remove(i+idx)
                mp['rd'].remove(i-idx)
                # path.pop()
        mp = {
            'col': set(),
            'rd': set(),
            'ld': set(),
        }
        self.ans = 0
        backtrack(0, 0)
        return self.ans
        