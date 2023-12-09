class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        total_sum = (n*(n+1))//2
        return total_sum - nums_sum
        