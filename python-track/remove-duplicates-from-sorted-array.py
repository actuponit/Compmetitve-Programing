class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = 1
        en = 2
        while st < len(nums):
            if nums[st] <= nums[st-1]:
                
                while en < len(nums) and nums[st-1] >= nums[en]:
                    en += 1
                if en >= len(nums):
                    break
                nums[st], nums[en] = nums[en], nums[st]
            st += 1
        return st
            
        