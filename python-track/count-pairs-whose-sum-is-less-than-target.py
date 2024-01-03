class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        limits = []
        for i in nums:
            limits.append(target - i)
        count = 0
        for i in range(len(limits)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < limits[i]:
                    count += 1
        return count
        