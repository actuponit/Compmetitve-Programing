class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        # Change one element of the array and if this pattern still exists return false
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                j = i + 1
                if j >= len(nums):
                    nums[i] = nums[i-1]
                    break
                if nums[i-1] > nums[j]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[j]
                break 
                
        # Go through the array agian to check there is another left
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
                
        return True