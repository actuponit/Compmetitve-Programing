class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
            
        for i, j in operations:
            nums[mp[i]] = j
            mp[j] = mp[i]
        return nums 
        