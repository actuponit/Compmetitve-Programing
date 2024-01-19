class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        s = 0
        total = sum(nums)
        for i in range(len(nums)):
            left = s 
            s += nums[i]
            right = total - s
            right_diff = right - ((len(nums) - 1 - i) * nums[i])
            left_diff = ((i) * nums[i]) - left
            ans.append(right_diff + left_diff)
        return ans

"""
1 4 6 8 10 
1 5 11 19 29
29 - 1 = 28 
28 - 4*1

29 - 5 = 24
1
24 - 3*4 + 1 - 4*1
"""
        