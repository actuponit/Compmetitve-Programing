class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(path):
            if len(path) == len(nums):
                sol.append(path.copy())
                return
            for i in nums:
                if not path or not i in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return sol 
        