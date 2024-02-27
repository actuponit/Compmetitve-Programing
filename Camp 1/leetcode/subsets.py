class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx, path):                 
            if len(path) < len(nums):
                sol.append(path.copy())
            elif len(path) == len(nums):
                sol.append(path.copy())
                return
                
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            # print("hi")
        sol = []
        backtrack(0, [])
        return sol