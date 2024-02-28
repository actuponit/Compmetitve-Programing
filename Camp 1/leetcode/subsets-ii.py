class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.prev = -11
        def backtrack(idx, path):                 
            if len(path) <= len(nums):
                
                sol.append(path.copy())
            if len(path) == len(nums):
                return
            
            for i in range(idx, len(nums)):                
                if self.prev == nums[i]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                self.prev = path.pop()
            # print("hi")
        sol = []
        nums.sort()
        backtrack(0, [])
        # sol = set(sol)
        return sol
        