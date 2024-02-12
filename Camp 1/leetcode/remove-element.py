class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        st, en = 0, len(nums) - 1 
        count = 0
        while st <= en:
            if nums[st] == val and nums[en] == val:
                nums[en] = -1
                en -= 1
                count += 1 
            elif nums[st] == val and nums[en] != val:
                nums[en], nums[st] = nums[st], nums[en]
                nums[en] = -1
                en -= 1
                st += 1
                count += 1 
            else:
                st += 1
        
        return len(nums) - count