class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        st = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0 and k > 0:
                k-=1
            elif nums[i] == 0:
                while nums[st] == 1:
                    st+=1
                st+=1
            maxi = max(maxi, i - st + 1)
        return maxi