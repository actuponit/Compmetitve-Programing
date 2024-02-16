class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = 0
        ans = float('-inf')
        for i in range(len(nums)):
            s += nums[i]
            ans = max(ans, s - m)
            m = min(m, s)
        return ans 
        