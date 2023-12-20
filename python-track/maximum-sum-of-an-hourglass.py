class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        sum = 0
        mini = 0
        for i in range(2, len(grid)):
            
            for j in range(2, len(grid[0])):                
                for k in range(3):
                    if k != 1:
                        sum += grid[i-k][j] + grid[i-k][j-1] + grid[i-k][j-2]
                    else:
                        sum += grid[i-1][j-1]
                mini = max(mini, sum)
                sum = 0

        return mini


        