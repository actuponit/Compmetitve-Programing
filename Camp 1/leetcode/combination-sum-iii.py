class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(idx, s, path):
            if len(path) == k and s == n:
                sol.append(path.copy())
                return
            if idx > 9:
                return
            if s > n or len(path) > k:
                return
            for i in range(idx, 10):
                path.append(i)
                backtrack(i+1, s+i, path)
                path.pop()
        sol = []
        backtrack(1, 0, [])
        return sol

        