class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        s = 0
        ans = 0
        while i < len(nums):
            zeros = -1
            while i < len(nums) and (nums[i] == 1 or zeros < 0):
                if nums[i] == 0:
                    zeros = i
                i += 1
            ans = max(ans, i - s - 1)
            s = zeros + 1
        return ans
        