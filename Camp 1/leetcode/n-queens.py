class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mp = {
            'row': set(),
            'col': set(),
            'rd': set(),
            'ld': set(),
        }
        def backtrack(path, mp):
            # print('hi')
            if len(path) == n:
                sol.append(path.copy())
                return
            if len(path) > n:
                return

            for i in range(n):
                if i in mp['row']:
                    continue

                if path and (i - path[-1][0] > 1 or path[-1][0] > i):
                    continue
                for j in range(n):
                    if j in mp['col'] or (i+j) in mp['ld'] or (i-j) in mp['rd']:
                        continue
                    path.append((i, j))
                    mp['row'].add(i)
                    mp['col'].add(j)
                    mp['ld'].add(i+j)
                    mp['rd'].add(i-j)
                    backtrack(path, mp)
                    mp['row'].remove(i)
                    mp['col'].remove(j)
                    mp['ld'].remove(i+j)
                    mp['rd'].remove(i-j)
                
                    self.prev = path.pop()
        sol = []
        backtrack([], mp)
        ans = []
        if not sol:
            return ''
        for i in sol:
            temp = []
            for j in i:
                st = '.'*j[1]
                
                st += 'Q'
                st += '.'*(n-len(st))
                temp.append(st)
            ans.append(temp)
        return ans