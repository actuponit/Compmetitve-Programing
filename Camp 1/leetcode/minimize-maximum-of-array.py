class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            ans = max(ans, ceil(s/(i+1)))
            
        return ans
# [13,13,20,0,8,9,9]
