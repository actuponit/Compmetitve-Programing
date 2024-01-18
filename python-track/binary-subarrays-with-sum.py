class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        st = 0
        s = 0
        ones = []
        if goal == 0:
            ans = 0
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    temp = 0
                    while i < len(nums) and nums[i] == 0:
                        temp += 1
                        ans += temp
                        i += 1
                i += 1
            return ans
        for i in range(len(nums)):
            if nums[i] == 1: ones.append(i)
        window_size = 1 if goal == 0 else goal
        ones.append(len(nums))
        ans = 0
        left = -1
        ans = 0
        for i in range(0, len(ones) - window_size):
            l = ones[i] - left
            r = ones[i + window_size] - ones[i + window_size-1]
            ans += (l*r)
            left = ones[i]
        return ans
        

"""
0 0 1 0 0
3 * 3

0 0 0 1 0 1 0 1 0
4 * 2
2 * 2
4 * 3
4 * 3
"""