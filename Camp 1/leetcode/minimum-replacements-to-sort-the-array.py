class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        spaces = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                spaces += ceil(nums[i - 1] / nums[i])
                nums[i - 1] = nums[i-1] // ceil(nums[i-1] / nums[i])
                # print(nums[i-1])
                spaces -= 1
        return spaces
                
                
        