class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right, left = [1]*len(nums), [1]*len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        
        for i in range(1, len(nums)):
            right[i] = right[i-1]*nums[len(nums)-i]
        
        ans = []
        
        for i in range(len(nums)):
            ans.append(right[len(nums)-i-1] * left[i]) 
        
        return ans

"""
r1 = r0*4 4
r2 = r1*3 12
r3 = r2*2 24
24 12 4 1
1  1  2 6
24 12 8 6
"""