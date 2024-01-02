class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[""] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = "W"

        g = [(1,0), (-1,0), (0, 1), (0, -1)]    
        for i, j in guards:
            grid[i][j] = "G"

        count = 0    
        for i, j in guards:
            for o, p in g:
                k, l = i+o, j+p
                while k > -1 and k < m and l > -1  and l < n and (grid[k][l] == '' or grid[k][l] == 'G1'):
                    count += 1 if grid[k][l] == '' else 0
                    grid[k][l] = 'G1'
                    k += o
                    l += p
        # print(count, len(guards), len(walls))
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "":
        #             count += 1
        return (n*m) - count - len(guards) - len(walls)

        