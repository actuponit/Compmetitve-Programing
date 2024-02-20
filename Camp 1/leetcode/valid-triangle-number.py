class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 1 2 2 3 3 4
        count = 0
        nums.sort()
        for i in range(len(nums)-1, 0, -1):
            r = i - 1
            l = 0
            while l < r:
                if nums[r] + nums[l] <= nums[i]:
                    l += 1
                else:
                    count += r - l
                    r -= 1
        return count
        