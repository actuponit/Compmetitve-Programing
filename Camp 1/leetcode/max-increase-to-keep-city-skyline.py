class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cols = [0] * n
        rows = [0] * n
        for i in range(n):
            rows[i] = max(grid[i])
        for i in range(n):
            cols[i] = max(grid[j][i] for j in range(n))
        ans = 0
        for i in range(n):
            for j in range(n):
                k = min(cols[j], rows[i]) - grid[i][j]
                ans += k if k > 0 else 0
        return ans
        