class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        largest_perimiter = 0
        
        for i in range(2, len(nums)):
            smallest_sum = nums[i-2] + nums[i-1]
            if nums[i] < smallest_sum:
                smallest_sum += nums[i]
                largest_perimiter = max(largest_perimiter, smallest_sum)
            
        return largest_perimiter
# 4 5 