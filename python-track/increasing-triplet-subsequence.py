class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        comp = float('inf')
        first = float('inf')
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if nums[i] > comp:
                    return True
                first = nums[i-1]
                comp = min(comp, nums[i])
            elif first < nums[i]:
                comp = nums[i]
        return False
        # [1,5,0,-1,-1,2,4,1,3]